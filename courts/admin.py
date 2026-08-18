from django.contrib import admin
from .models import (
    SiteSetting, HeroSlide, TennisCourt, CourtSlot,
    Reservation, GalleryCategory, GalleryItem,
    TrainingClass, ClassEnrollment
)

admin.site.site_header = "پنل مدیریت مجموعه تنیس رویال کورت (Royal Court)"
admin.site.site_title = "مدیریت رویال کورت"
admin.site.index_title = "مدیریت بخش‌ها، تقویم سانس‌ها و رزروها"


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'manager_name', 'phone_number', 'base_session_price', 'default_discount_percent')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(TennisCourt)
class TennisCourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'court_type', 'is_active')
    list_editable = ('is_active',)


@admin.register(CourtSlot)
class CourtSlotAdmin(admin.ModelAdmin):
    list_display = ('court', 'jalali_date', 'date', 'start_time', 'end_time', 'price', 'discount_percent', 'final_price', 'is_booked', 'is_blocked')
    list_filter = ('court', 'is_booked', 'is_blocked', 'date')
    list_editable = ('price', 'discount_percent', 'is_booked', 'is_blocked')
    search_fields = ('jalali_date', 'court__name')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'full_name', 'phone_number', 'slot', 'created_at', 'is_confirmed')
    list_filter = ('is_confirmed', 'created_at')
    search_fields = ('full_name', 'phone_number', 'tracking_code')
    readonly_fields = ('tracking_code', 'created_at')


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(TrainingClass)
class TrainingClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'coach_name', 'level', 'tuition', 'is_active')
    list_editable = ('is_active', 'tuition')
    search_fields = ('title', 'coach_name')


@admin.register(ClassEnrollment)
class ClassEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'training_class', 'created_at')
    list_filter = ('training_class', 'created_at')
    search_fields = ('full_name', 'phone_number')

