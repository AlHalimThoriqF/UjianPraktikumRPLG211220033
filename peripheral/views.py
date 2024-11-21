from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Mouse, Monitor, Keyboard, Headset, Webcam, KabelKonektor

def index(request):
    return render(request, "index.html")
    
# Headset Views
def headset_index(request):
    context = {
        'headset_list': Headset.objects.all()
    }
    return render(request, "headset/index.html", context)

def headset_add(request):
    return render(request, "headset/form_add.html")

def headset_save(request):
    headset = Headset(
        nama=request.POST['nama'],
        merek=request.POST['merek'],
        tipe=request.POST['tipe'],
        koneksi=request.POST['koneksi'],
        kualitas_suara=request.POST['kualitas_suara'],
        mikrofon=True if request.POST.get('mikrofon') == 'on' else False,
        harga=int(request.POST['harga']),
        stok=int(request.POST['stok']),
    )
    headset.save()
    return HttpResponseRedirect(reverse('headset.index'))

def headset_delete(request, headset_id):
    headset = get_object_or_404(Headset, pk=headset_id)
    headset.delete()
    return HttpResponseRedirect(reverse('headset.index'))

def headset_edit(request, headset_id):
    headset = get_object_or_404(Headset, pk=headset_id)
    context = {
        'id': headset_id,
        'nama': headset.nama,
        'merek': headset.merek,
        'tipe': headset.tipe,
        'koneksi': headset.koneksi,
        'kualitas_suara': headset.kualitas_suara,
        'mikrofon': headset.mikrofon,
        'harga': headset.harga,
        'stok': headset.stok,
    }
    return render(request, 'headset/form_edit.html', context)

def headset_update(request, headset_id):
    headset = get_object_or_404(Headset, pk=headset_id)
    headset.nama = request.POST['nama']
    headset.merek = request.POST['merek']
    headset.tipe = request.POST['tipe']
    headset.koneksi = request.POST['koneksi']
    headset.kualitas_suara = request.POST['kualitas_suara']
    headset.mikrofon = True if request.POST.get('mikrofon') == 'on' else False
    headset.harga = int(request.POST['harga'])
    headset.stok = int(request.POST['stok'])
    headset.save()
    return HttpResponseRedirect(reverse('headset.index'))

# KabelKonektor Views
def kabelkonektor_index(request):
    context = {
        'kabelkonektor_list': KabelKonektor.objects.all()
    }
    return render(request, "kabelkonektor/index.html", context)

def kabelkonektor_add(request):
    return render(request, "kabelkonektor/form_add.html")

def kabelkonektor_save(request):
    kabelkonektor = KabelKonektor(
        nama=request.POST['nama'],
        merek=request.POST['merek'],
        tipe_kabel=request.POST['tipe_kabel'],
        harga=int(request.POST['harga']),
        stok=int(request.POST['stok']),
    )
    kabelkonektor.save()
    return HttpResponseRedirect(reverse('kabelkonektor.index'))

def kabelkonektor_delete(request, kabelkonektor_id):
    kabelkonektor = get_object_or_404(KabelKonektor, pk=kabelkonektor_id)
    kabelkonektor.delete()
    return HttpResponseRedirect(reverse('kabelkonektor.index'))

def kabelkonektor_edit(request, kabelkonektor_id):
    kabelkonektor = get_object_or_404(KabelKonektor, pk=kabelkonektor_id)
    context = {
        'id': kabelkonektor_id,
        'nama': kabelkonektor.nama,
        'merek': kabelkonektor.merek,
        'tipe_kabel': kabelkonektor.tipe_kabel,
        'harga': kabelkonektor.harga,
        'stok': kabelkonektor.stok,
    }
    return render(request, 'kabelkonektor/form_edit.html', context)

def kabelkonektor_update(request, kabelkonektor_id):
    kabelkonektor = get_object_or_404(KabelKonektor, pk=kabelkonektor_id)
    kabelkonektor.nama = request.POST['nama']
    kabelkonektor.merek = request.POST['merek']
    kabelkonektor.tipe_kabel = request.POST['tipe_kabel']
    kabelkonektor.harga = int(request.POST['harga'])
    kabelkonektor.stok = int(request.POST['stok'])
    kabelkonektor.save()
    return HttpResponseRedirect(reverse('kabelkonektor.index'))

# Keyboard Views
def keyboard_index(request):
    context = {
        'keyboard_list': Keyboard.objects.all()
    }
    return render(request, "keyboard/index.html", context)

def keyboard_add(request):
    return render(request, "keyboard/form_add.html")

def keyboard_save(request):
    keyboard = Keyboard(
        nama=request.POST['nama'],
        merek=request.POST['merek'],
        jenis_switch=request.POST['jenis_switch'],
        fitur=request.POST['fitur'],
        harga=int(request.POST['harga']),
        stok=int(request.POST['stok']),
    )
    keyboard.save()
    return HttpResponseRedirect(reverse('keyboard.index'))

def keyboard_delete(request, keyboard_id):
    keyboard = get_object_or_404(Keyboard, pk=keyboard_id)
    keyboard.delete()
    return HttpResponseRedirect(reverse('keyboard.index'))

def keyboard_edit(request, keyboard_id):
    keyboard = get_object_or_404(Keyboard, pk=keyboard_id)
    context = {
        'id': keyboard_id,
        'nama': keyboard.nama,
        'merek': keyboard.merek,
        'jenis_switch': keyboard.jenis_switch,
        'fitur': keyboard.fitur,
        'harga': keyboard.harga,
        'stok': keyboard.stok,
    }
    return render(request, 'keyboard/form_edit.html', context)

def keyboard_update(request, keyboard_id):
    keyboard = get_object_or_404(Keyboard, pk=keyboard_id)
    keyboard.nama = request.POST['nama']
    keyboard.merek = request.POST['merek']
    keyboard.jenis_switch = request.POST['jenis_switch']
    keyboard.fitur = request.POST['fitur']
    keyboard.harga = int(request.POST['harga'])
    keyboard.stok = int(request.POST['stok'])
    keyboard.save()
    return HttpResponseRedirect(reverse('keyboard.index'))

# Mouse Views
def mouse_index(request):
    context = {
        'mouse_list': Mouse.objects.all()
    }
    return render(request, "mouse/index.html", context)

def mouse_add(request):
    return render(request, "mouse/form_add.html")

def mouse_save(request):
    mouse = Mouse(
        nama=request.POST['nama'],
        merek=request.POST['merek'],
        jenis_koneksi=request.POST['jenis_koneksi'],
        dpi_maksimum=int(request.POST['dpi_maksimum']),
        harga=int(request.POST['harga']),
        stok=int(request.POST['stok']),
    )
    mouse.save()
    return HttpResponseRedirect(reverse('mouse.index'))

def mouse_delete(request, mouse_id):
    mouse = get_object_or_404(Mouse, pk=mouse_id)
    mouse.delete()
    return HttpResponseRedirect(reverse('mouse.index'))

def mouse_edit(request, mouse_id):
    mouse = get_object_or_404(Mouse, pk=mouse_id)
    context = {
        'id': mouse_id,
        'nama': mouse.nama,
        'merek': mouse.merek,
        'jenis_koneksi': mouse.jenis_koneksi,
        'dpi_maksimum': mouse.dpi_maksimum,
        'harga': mouse.harga,
        'stok': mouse.stok,
    }
    return render(request, 'mouse/form_edit.html', context)

def mouse_update(request, mouse_id):
    mouse = get_object_or_404(Mouse, pk=mouse_id)
    mouse.nama = request.POST['nama']
    mouse.merek = request.POST['merek']
    mouse.jenis_koneksi = request.POST['jenis_koneksi']
    mouse.dpi_maksimum = int(request.POST['dpi_maksimum'])
    mouse.harga = int(request.POST['harga'])
    mouse.stok = int(request.POST['stok'])
    mouse.save()
    return HttpResponseRedirect(reverse('mouse.index'))

# Monitor Views
def monitor_index(request):
    context = {
        'monitor_list': Monitor.objects.all()
    }
    return render(request, "monitor/index.html", context)

def monitor_add(request):
    return render(request, "monitor/form_add.html")

def monitor_save(request):
    monitor = Monitor(
        nama=request.POST['nama'],
        merek=request.POST['merek'],
        resolusi=request.POST['resolusi'],
        ukuran_inci=float(request.POST['ukuran_inci']),
        harga=int(request.POST['harga']),
        stok=int(request.POST['stok']),
    )
    monitor.save()
    return HttpResponseRedirect(reverse('monitor.index'))

def monitor_delete(request, monitor_id):
    monitor = get_object_or_404(Monitor, pk=monitor_id)
    monitor.delete()
    return HttpResponseRedirect(reverse('monitor.index'))

def monitor_edit(request, monitor_id):
    monitor = get_object_or_404(Monitor, pk=monitor_id)
    context = {
        'id': monitor_id,
        'nama': monitor.nama,
        'merek': monitor.merek,
        'resolusi': monitor.resolusi,
        'ukuran_inci': monitor.ukuran_inci,
        'harga': monitor.harga,
        'stok': monitor.stok,
    }
    return render(request, 'monitor/form_edit.html', context)

def monitor_update(request, monitor_id):
    monitor = get_object_or_404(Monitor, pk=monitor_id)
    monitor.nama = request.POST['nama']
    monitor.merek = request.POST['merek']
    monitor.resolusi = request.POST['resolusi']
    monitor.ukuran_inci = (request.POST['ukuran_inci'])
    monitor.harga = int(request.POST['harga'])
    monitor.stok = int(request.POST['stok'])
    monitor.save()
    return HttpResponseRedirect(reverse('monitor.index'))

# Webcam Views
def webcam_index(request):
    context = {
        'webcam_list': Webcam.objects.all()
    }
    return render(request, "webcam/index.html", context)

def webcam_add(request):
    return render(request, "webcam/form_add.html")

def webcam_save(request):
    webcam = Webcam(
        nama=request.POST['nama'],
        merek=request.POST['merek'],
        resolusi_video=request.POST['resolusi_video'],
        fps_maksimum=int(request.POST['fps_maksimum']),
        harga=int(request.POST['harga']),
        stok=int(request.POST['stok']),
    )
    webcam.save()
    return HttpResponseRedirect(reverse('webcam.index'))

def webcam_delete(request, webcam_id):
    webcam = get_object_or_404(Webcam, pk=webcam_id)
    webcam.delete()
    return HttpResponseRedirect(reverse('webcam.index'))

def webcam_edit(request, webcam_id):
    webcam = get_object_or_404(Webcam, pk=webcam_id)
    context = {
        'id': webcam_id,
        'nama': webcam.nama,
        'merek': webcam.merek,
        'resolusi_video': webcam.resolusi_video,
        'fps_maksimum': webcam.fps_maksimum,
        'harga': webcam.harga,
        'stok': webcam.stok,
    }
    return render(request, 'webcam/form_edit.html', context)

def webcam_update(request, webcam_id):
    webcam = get_object_or_404(Webcam, pk=webcam_id)
    webcam.nama = request.POST['nama']
    webcam.merek = request.POST['merek']
    webcam.resolusi_video = request.POST['resolusi_video']
    webcam.fps_maksimum = int(request.POST['fps_maksimum'])
    webcam.harga = int(request.POST['harga'])
    webcam.stok = int(request.POST['stok'])
    webcam.save()
    return HttpResponseRedirect(reverse('webcam.index'))