from django.urls import path
from . import views
urlpatterns = [
  path('',views.index,name='peripheral.index'),
  
  # Headset URLs
  path('headset/', views.headset_index, name='headset.index'),
  path('headset/tambah/', views.headset_add, name='headset.add'),
  path('headset/simpan/', views.headset_save, name='headset.save'),
  path('headset/<int:headset_id>/hapus/', views.headset_delete, name='headset.delete'),
  path('headset/<int:headset_id>/edit/', views.headset_edit, name='headset.edit'),
  path('headset/<int:headset_id>/update/', views.headset_update, name='headset.update'),

  # KabelKonektor URLs
  path('kabelkonektor/', views.kabelkonektor_index, name='kabelkonektor.index'),
  path('kabelkonektor/tambah/', views.kabelkonektor_add, name='kabelkonektor.add'),
  path('kabelkonektor/simpan/', views.kabelkonektor_save, name='kabelkonektor.save'),
  path('kabelkonektor/<int:kabelkonektor_id>/hapus/', views.kabelkonektor_delete, name='kabelkonektor.delete'),
  path('kabelkonektor/<int:kabelkonektor_id>/edit/', views.kabelkonektor_edit, name='kabelkonektor.edit'),
  path('kabelkonektor/<int:kabelkonektor_id>/update/', views.kabelkonektor_update, name='kabelkonektor.update'),

  # Keyboard URLs
  path('keyboard/', views.keyboard_index, name='keyboard.index'),
  path('keyboard/tambah/', views.keyboard_add, name='keyboard.add'),
  path('keyboard/simpan/', views.keyboard_save, name='keyboard.save'),
  path('keyboard/<int:keyboard_id>/hapus/', views.keyboard_delete, name='keyboard.delete'),
  path('keyboard/<int:keyboard_id>/edit/', views.keyboard_edit, name='keyboard.edit'),
  path('keyboard/<int:keyboard_id>/update/', views.keyboard_update, name='keyboard.update'),
  
  # Monitor URLs
  path('monitor/', views.monitor_index, name='monitor.index'),
  path('monitor/tambah/', views.monitor_add, name='monitor.add'),
  path('monitor/simpan/', views.monitor_save, name='monitor.save'),
  path('monitor/<int:monitor_id>/hapus/', views.monitor_delete, name='monitor.delete'),
  path('monitor/<int:monitor_id>/edit/', views.monitor_edit, name='monitor.edit'),
  path('monitor/<int:monitor_id>/update/', views.monitor_update, name='monitor.update'),
  
  # Mouse URLs
  path('mouse/', views.mouse_index, name='mouse.index'),
  path('mouse/tambah/', views.mouse_add, name='mouse.add'),
  path('mouse/simpan/', views.mouse_save, name='mouse.save'),
  path('mouse/<int:mouse_id>/hapus/', views.mouse_delete, name='mouse.delete'),
  path('mouse/<int:mouse_id>/edit/', views.mouse_edit, name='mouse.edit'),
  path('mouse/<int:mouse_id>/update/', views.mouse_update, name='mouse.update'),

  # WebCam URLs
  path('webcam/', views.webcam_index, name='webcam.index'),
  path('webcam/tambah/', views.webcam_add, name='webcam.add'),
  path('webcam/simpan/', views.webcam_save, name='webcam.save'),
  path('webcam/<int:webcam_id>/hapus/', views.webcam_delete, name='webcam.delete'),
  path('webcam/<int:webcam_id>/edit/', views.webcam_edit, name='webcam.edit'),
  path('webcam/<int:webcam_id>/update/', views.webcam_update, name='webcam.update'),

  ]