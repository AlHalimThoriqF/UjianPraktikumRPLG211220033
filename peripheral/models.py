from django.db import models

class Headset(models.Model):
    nama = models.CharField(max_length=200)
    merek = models.CharField(max_length=100)
    tipe = models.CharField(
        max_length=10,
        choices=[("wired", "Wired"), ("wireless", "Wireless")],
        default="wired",
    )
    koneksi = models.CharField(
        max_length=50,
        choices=[("jack", "3.5mm Jack"), ("usb", "USB"), ("bluetooth", "Bluetooth")],
        default="jack",
    )
    kualitas_suara = models.CharField(
        max_length=50,
        choices=[("stereo", "Stereo"), ("surround", "Surround"), ("mono", "Mono")],
        default="stereo",
    )
    mikrofon = models.BooleanField(default=False)
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama


class KabelKonektor(models.Model):
    nama = models.CharField(max_length=200)
    merek = models.CharField(max_length=100)
    tipe_kabel = models.CharField(
        max_length=100,
        choices=[
            ("HDMI", "HDMI"),
            ("USB", "USB"),
            ("Ethernet", "Ethernet"),
            ("Lainnya", "Lainnya"),
        ],
    )
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama


class Monitor(models.Model):
    nama = models.CharField(max_length=200)
    merek = models.CharField(max_length=100)
    resolusi = models.CharField(
        max_length=50,
        choices=[
            ("1366x768", "HD (1366x768)"),
            ("1920x1080", "Full HD (1920x1080)"),
            ("2560x1440", "QHD (2560x1440)"),
            ("3840x2160", "4K (3840x2160)"),
            ("5120x2880", "5K (5120x2880)"),
            ("7680x4320", "8K (7680x4320)"),
        ],
    )
    ukuran_inci = models.DecimalField(max_digits=4, decimal_places=1)
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama


class Mouse(models.Model):
    nama = models.CharField(max_length=200)
    merek = models.CharField(max_length=100)
    jenis_koneksi = models.CharField(
        max_length=50,
        choices=[
            ("Wireless", "Wireless"),
            ("Wired", "Wired"),
            ("Hybrid", "Wireless + Wired"),
        ],
        default="Wired",
    )
    dpi_maksimum = models.PositiveIntegerField(
        help_text="Dots Per Inch maksimum yang didukung",
        choices=[
            (800, "800 DPI"),
            (1600, "1600 DPI"),
            (3200, "3200 DPI"),
            (6400, "6400 DPI"),
            (12000, "12000 DPI"),
            (16000, "16000 DPI"),
            (20000, "20000 DPI"),
            (25600, "25600 DPI"),
        ],
        default=800,
    )
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama


class Keyboard(models.Model):
    nama = models.CharField(max_length=200)
    merek = models.CharField(max_length=100)
    jenis_switch = models.CharField(
        max_length=50,
        choices=[
            ("Membran", "Membran"),
            ("Mecha-Membrane", "Mecha-Membrane"),
            ("Mechanical-Blue", "Mechanical Blue Switch"),
            ("Mechanical-Red", "Mechanical Red Switch"),
            ("Mechanical-Brown", "Mechanical Brown Switch"),
            ("Optical", "Optical Switch"),
        ],
        default="Membran",
    )
    fitur = models.CharField(
        max_length=50,
        choices=[
            ("Basic", "Basic (No Backlight)"),
            ("Backlit", "Single Color Backlit"),
            ("RGB", "RGB Backlit"),
            ("RGB-Pro", "RGB + Macro Keys"),
        ],
        default="Basic",
    )
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama


class Webcam(models.Model):
    nama = models.CharField(max_length=200)
    merek = models.CharField(max_length=100)
    resolusi_video = models.CharField(
        max_length=50,
        choices=[
            ("720p", "HD (1280x720)"),
            ("1080p", "Full HD (1920x1080)"),
            ("2K", "QHD (2560x1440)"),
            ("4K", "Ultra HD (3840x2160)"),
        ],
        default="1080p",
    )
    fps_maksimum = models.PositiveIntegerField(
        choices=[(30, "30 FPS"), (60, "60 FPS"), (120, "120 FPS")],
        default=30,
    )
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama
