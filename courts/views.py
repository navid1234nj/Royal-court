import json
import random
import string
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.utils import timezone
from django.db import transaction
from .models import (
    SiteSetting, HeroSlide, TennisCourt, CourtSlot,
    Reservation, GalleryCategory, GalleryItem,
    TrainingClass, ClassEnrollment
)


def get_site_config():
    config, created = SiteSetting.objects.get_or_create(id=1)
    return config


def index(request):
    config = get_site_config()
    slides = HeroSlide.objects.filter(is_active=True).order_by('order')
    courts = TennisCourt.objects.filter(is_active=True)
    gallery_categories = GalleryCategory.objects.all()
    gallery_items = GalleryItem.objects.all().order_by('-created_at')
    training_classes = TrainingClass.objects.filter(is_active=True)

    # Get distinct available dates for slot tabs
    slots = CourtSlot.objects.filter(is_blocked=False).order_by('date', 'start_time')

    context = {
        'config': config,
        'slides': slides,
        'courts': courts,
        'gallery_categories': gallery_categories,
        'gallery_items': gallery_items,
        'training_classes': training_classes,
        'slots': slots,
    }
    return render(request, 'index.html', context)


@require_GET
def api_get_slots(request):
    court_id = request.GET.get('court_id')
    date_str = request.GET.get('date')

    slots_qs = CourtSlot.objects.all().order_by('date', 'start_time')

    if court_id and court_id != 'all':
        slots_qs = slots_qs.filter(court_id=court_id)

    if date_str:
        slots_qs = (
            slots_qs.filter(jalali_date__icontains=date_str)
            | slots_qs.filter(date=date_str)
        )

    data = []

    for slot in slots_qs:
        data.append({
            'id': slot.id,
            'court_id': slot.court.id,
            'court_name': slot.court.name,
            'date': str(slot.date),
            'jalali_date': slot.jalali_date,
            'start_time': slot.start_time.strftime('%H:%M'),
            'end_time': slot.end_time.strftime('%H:%M'),
            'price': slot.price,
            'discount_percent': slot.discount_percent,
            'final_price': slot.final_price,
            'is_booked': slot.is_booked,
            'is_blocked': slot.is_blocked,
        })

    return JsonResponse({
        'success': True,
        'slots': data
    })


@csrf_exempt
@require_POST
def api_reserve_slot(request):
    try:
        data = json.loads(request.body)
    except Exception:
        data = request.POST

    slot_id = data.get('slot_id')
    full_name = data.get('full_name', '').strip()
    phone_number = data.get('phone_number', '').strip()

    if not slot_id or not full_name or not phone_number:
        return JsonResponse({
            'success': False,
            'message': 'لطفاً تمامی اطلاعات (نام و شماره تماس) را وارد نمایید.'
        }, status=400)

    try:
        with transaction.atomic():
            slot = (
                CourtSlot.objects
                .select_for_update()
                .get(id=slot_id)
            )

            if slot.is_booked:
                return JsonResponse({
                    'success': False,
                    'message': 'متاسفانه این سانس قبلاً رزرو شده است.'
                }, status=400)

            if slot.is_blocked:
                return JsonResponse({
                    'success': False,
                    'message': 'این سانس غیرقابل رزرو می‌باشد.'
                }, status=400)

            # Generate tracking code
            code_suffix = ''.join(
                random.choices(string.digits, k=5)
            )
            tracking_code = f"RC-{code_suffix}"

            slot.is_booked = True
            slot.save(update_fields=['is_booked'])

            reservation = Reservation.objects.create(
                slot=slot,
                full_name=full_name,
                phone_number=phone_number,
                tracking_code=tracking_code,
                is_confirmed=True
            )

        return JsonResponse({
            'success': True,
            'message': 'رزرو شما با موفقیت در سیستم ثبت گردید.',
            'tracking_code': tracking_code,
            'slot_info': {
                'court_name': slot.court.name,
                'jalali_date': slot.jalali_date,
                'time': (
                    f"{slot.start_time.strftime('%H:%M')} "
                    f"تا {slot.end_time.strftime('%H:%M')}"
                ),
                'price': f"{slot.final_price:,} تومان",
                'full_name': full_name,
                'phone_number': phone_number
            }
        })

    except CourtSlot.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'سانس مورد نظر یافت نشد.'
        }, status=404)


@csrf_exempt
@require_POST
def api_enroll_class(request):
    try:
        data = json.loads(request.body)
    except Exception:
        data = request.POST

    class_id = data.get('class_id')
    full_name = data.get('full_name', '').strip()
    phone_number = data.get('phone_number', '').strip()
    notes = data.get('notes', '').strip()

    if not class_id or not full_name or not phone_number:
        return JsonResponse({
            'success': False,
            'message': 'لطفاً تمامی فیلدهای اجباری را تکمیل کنید.'
        }, status=400)

    try:
        t_class = TrainingClass.objects.get(id=class_id)
    except TrainingClass.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'کلاس مورد نظر یافت نشد.'
        }, status=404)

    ClassEnrollment.objects.create(
        training_class=t_class,
        full_name=full_name,
        phone_number=phone_number,
        notes=notes
    )

    return JsonResponse({
        'success': True,
        'message': (
            f'ثبت‌نام اولیه شما در {t_class.title} با موفقیت انجام شد. '
            'کارشناسان ما جهت هماهنگی نهایی با شما تماس خواهند گرفت.'
        )
    })
