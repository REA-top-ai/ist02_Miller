#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>

struct BitmapHeaders {
    std::uint32_t file_size;
    std::uint32_t reserved;
    std::uint32_t data_offset;
    std::uint32_t dib_size;
    std::int32_t width;
    std::int32_t height;
    std::uint16_t planes;
    std::uint16_t bit_count;
    std::uint32_t compression;
    std::uint32_t image_size;
    std::int32_t x_pixels_per_meter;
    std::int32_t y_pixels_per_meter;
    std::uint32_t colors_used;
    std::uint32_t colors_important;
};

struct Pixel {
    unsigned char b, g, r;
};

static std::uint32_t read_int(const unsigned char* bytes) {
    return std::uint32_t{bytes[0]}
         | (std::uint32_t{bytes[1]} << 8)
         | (std::uint32_t{bytes[2]} << 16)
         | (std::uint32_t{bytes[3]} << 24);
}

static std::uint16_t read_short(const unsigned char* bytes) {
    return static_cast<std::uint16_t>(bytes[0] | (std::uint16_t{bytes[1]} << 8));
}

static bool load_raw_file_data(std::ifstream& file, unsigned char* buffer,
                               std::streamsize size, std::streamoff pos = 0) {
    file.seekg(pos, std::ios::beg);
    return static_cast<bool>(file.read(reinterpret_cast<char*>(buffer), size));
}

static bool load_headers(std::ifstream& file, BitmapHeaders& header) {
    unsigned char buffer[54]{};
    if (!load_raw_file_data(file, buffer, sizeof(buffer))) {
        std::cerr << "Ошибка чтения заголовка BMP\n";
        return false;
    }
    if (buffer[0] != 'B' || buffer[1] != 'M') {
        std::cerr << "Не BMP файл\n";
        return false;
    }
    header.file_size = read_int(buffer + 2);
    header.reserved = read_int(buffer + 6);
    header.data_offset = read_int(buffer + 10);
    header.dib_size = read_int(buffer + 14);
    header.width = std::bit_cast<std::int32_t>(read_int(buffer + 18));
    header.height = std::bit_cast<std::int32_t>(read_int(buffer + 22));
    header.planes = read_short(buffer + 26);
    header.bit_count = read_short(buffer + 28);
    header.compression = read_int(buffer + 30);
    header.image_size = read_int(buffer + 34);
    header.x_pixels_per_meter = std::bit_cast<std::int32_t>(read_int(buffer + 38));
    header.y_pixels_per_meter = std::bit_cast<std::int32_t>(read_int(buffer + 42));
    header.colors_used = read_int(buffer + 46);
    header.colors_important = read_int(buffer + 50);

    if (header.dib_size < 40) {
        std::cerr << "Неподдерживаемый заголовок DIB для BMP-файла\n";
        return false;
    }
    return true;
}

static void print_bitmap_headers(const BitmapHeaders& header) {
    std::cout << "File Size: " << header.file_size << '\n'
              << "Reserved: " << header.reserved << '\n'
              << "Data Offset: " << header.data_offset << '\n'
              << "Size: " << header.dib_size << '\n'
              << "Width: " << header.width << '\n'
              << "Height: " << header.height << '\n'
              << "Planes: " << header.planes << '\n'
              << "Bit Count: " << header.bit_count << '\n'
              << "Compression: " << header.compression << '\n'
              << "Image Size: " << header.image_size << '\n'
              << "X Pixels Per Meter: " << header.x_pixels_per_meter << '\n'
              << "Y Pixels Per Meter: " << header.y_pixels_per_meter << '\n'
              << "Colors Used: " << header.colors_used << '\n'
              << "Colors Important: " << header.colors_important << '\n';
}

static bool validate_pixel_format(const BitmapHeaders& header) {
    if (header.planes != 1 ||
        header.bit_count != 24 || header.compression != 0) {
        std::cerr << "Поддерживаются только несжатые 24-битные BMP-файлы с заголовком Windows DIB.\n";
        return false;
    }
    if (header.width <= 0 || header.height == 0 ||
        header.data_offset < 14ULL + header.dib_size) {
        std::cerr << "Недопустимые размеры BMP или неверное смещение данных.\n";
        return false;
    }
    return true;
}

// Координаты начинаются в верхнем левом углу видимого изображения
static bool get_pixel(std::ifstream& file, const BitmapHeaders& header,
                      std::int64_t row_size, std::int64_t height,
                      std::int64_t x, std::int64_t y, Pixel& pixel) {
    const std::int64_t file_y = header.height > 0 ? height - 1 - y : y;
    const std::int64_t position = header.data_offset + file_y * row_size + x * 3;
    unsigned char bytes[3]{};
    if (!load_raw_file_data(file, bytes, sizeof(bytes), position)) {
        return false;
    }
    pixel = {bytes[0], bytes[1], bytes[2]};
    return true;
}

static void print_pixel(const char* corner, const Pixel& pixel) {
    std::cout << corner
              << ": R: " << static_cast<int>(pixel.r)
              << " G: " << static_cast<int>(pixel.g)
              << " B: " << static_cast<int>(pixel.b) << '\n';
}

int main(int argc, char** argv) {
    const char* path = argc > 1 ? argv[1]
        : "C:\\Users\\User\\CLionProjects\\Bitmap\\Images\\lena.bmp";
    std::ifstream file(path, std::ios::binary);
    if (!file) {
        std::cerr << "Не удалось открыть файл: " << path << '\n';
        return 1;
    }
    BitmapHeaders header{};
    if (!load_headers(file, header)) {
        return 1;
    }
    print_bitmap_headers(header);
    std::cout << std::endl;
    if (!validate_pixel_format(header)) {
        return 1;
    }

    const std::int64_t width = header.width;
    const std::int64_t height = header.height < 0
        ? -std::int64_t{header.height} : header.height;
    // Каждая строка дополняется до размера, кратного четырем байтам
    const std::int64_t row_size = (width * 3 + 3) / 4 * 4;
    file.seekg(0, std::ios::end);
    const std::streamoff file_size = file.tellg();
    if (file_size < 0 || file_size < header.data_offset + row_size * height) {
        std::cerr << "Данные пикселей BMP-файла обрезаны.\n";
        return 1;
    }

    Pixel upper_left{}, upper_right{}, lower_left{}, lower_right{};
    if (!get_pixel(file, header, row_size, height, 0, 0, upper_left) ||
        !get_pixel(file, header, row_size, height, width - 1, 0, upper_right) ||
        !get_pixel(file, header, row_size, height, 0, height - 1, lower_left) ||
        !get_pixel(file, header, row_size, height, width - 1, height - 1, lower_right)) {
        std::cerr << "Не удалось прочитать угловые пиксели.\n";
        return 1;
    }
    print_pixel("Upper-left", upper_left);
    print_pixel("Upper-right", upper_right);
    print_pixel("Lower-left", lower_left);
    print_pixel("Lower-right", lower_right);
    return 0;
}
