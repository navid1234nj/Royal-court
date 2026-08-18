from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import datetime, timedelta, time
from courts.models import (
    SiteSetting, HeroSlide, TennisCourt, CourtSlot,
    Reservation, GalleryCategory, GalleryItem, TrainingClass
)

class Command(BaseCommand):
    help = 'Populates initial realistic seed data for Royal Court'

    def handle(self, *args, **options):
        self.stdout.write("Seeding database for Royal Court...")

        # Create Superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@royalcourt.ir', 'admin123')
            self.stdout.write("Created superuser: admin / admin123")

        # Create Site Setting
        config, created = SiteSetting.objects.get_or_create(id=1)
        config.site_name = "Royal Court"
        config.site_title_fa = "مجموعه تنیس خاکی رویال کورت"
        config.manager_name = "محمد عتبات"
        config.phone_number = "021-22889900 | 09121000200"
        config.instagram = "@royalcourt_tennis"
        config.address = "تهران، خیابان فرشته، مجموعه ورزشی و تنیس VIP رویال کورت"
        config.hero_title = "تجربه‌ای لوکس و حرفه‌ای در استثنایی‌ترین زمین‌های تنیس خاکی"
        config.hero_subtitle = "زمین‌های خاکی سرخ بین‌المللی با زیرسازی استاندارد ITF، نورپردازی ال‌ای‌دی دید در شب، کلاب‌هاوس مدرن و رزرو آنلاین ۲۴ ساعته بدون نیاز به ثبت‌نام"
        config.about_title = "درباره مجموعه تنیس رویال کورت"
        config.about_text = "مجموعه تنیس رویال کورت با مدیریت جناب آقای محمد عتبات، با بهره‌گیری از بالاترین استانداردهای بین‌المللی ITF طراحی و ساخته شده است. مجموعه دارای زمین‌های خاکی سرخ حرفه‌ای (Red Clay)، سیستم هوشمند رزرو سانس آنلاین، نورپردازی پیشرفته شبانه، رختکن و دوش مدرن، بوفه و کلاب‌هاوس اختصاصی، و تیم حرفه‌ای اساتید رسمی فدراسیون تنیس می‌باشد."
        config.base_session_price = 500000
        config.default_discount_percent = 15
        config.price_notice_text = "⚡ پیشنهاد ویژه: ۱۵٪ تخفیف برای کلیه سانس‌های صبحگاهی و پایان هفته فعال گردید!"
        config.save()

        # Create Tennis Courts
        c1, _ = TennisCourt.objects.get_or_create(
            name="زمین شماره ۱ (VIP مرکزی)",
            defaults={"court_type": "تنیس خاکی سرخ (Red Clay)", "description": "زمین مرکزی با ابعاد استاندارد مسابقاتی و جایگاه تماشاگران"}
        )
        c2, _ = TennisCourt.objects.get_or_create(
            name="زمین شماره ۲ (تمرینی اختصاصی)",
            defaults={"court_type": "تنیس خاکی سرخ (Red Clay)", "description": "زمین اختصاصی برای تمرینات شخصی، آموزشی و بازی‌های تک‌به‌تک"}
        )

        # Create Gallery Categories & Items
        cat1, _ = GalleryCategory.objects.get_or_create(title="زمین‌ها و فضا")
        cat2, _ = GalleryCategory.objects.get_or_create(title="مسابقات و رویدادها")
        cat3, _ = GalleryCategory.objects.get_or_create(title="کلاس‌های آموزشی")

        # Create Training Classes
        if not TrainingClass.objects.exists():
            TrainingClass.objects.create(
                title="دوره خصوصی تنیس خاکی (تک‌نفره)",
                coach_name="استاد محمد عتبات و سرمربیان ارشد",
                level="مبتدی، متوسطه و حرفه‌ای",
                duration="۱۰ جلسه ۱ ساعته",
                tuition=6500000,
                schedule_info="هماهنگی ساعت دقیق سانس با هنرجو (تمام روزهای هفته)",
                features_list="آموزش تخصصی تکنیک‌های فورهند، بک‌هند و سرویس\nاصلاح آنالیز ویدئویی حرکات\nارائه راکت و توپ تمرینی رایگان در طول دوره\nامکان تغییر زمان جلسه با هماهنگی ۲۴ ساعت قبل",
                is_active=True
            )
            TrainingClass.objects.create(
                title="آکادمی تنیس کودکان و نوجوانان",
                coach_name="تیم مربیان تخصصی رده سنی فدراسیون",
                level="کودکان ۵ الی ۱۵ سال",
                duration="۱۲ جلسه ۱ ساعته",
                tuition=4200000,
                schedule_info="روزهای زوج - ساعت ۱۶:۰۰ الی ۱۸:۰۰",
                features_list="توپ‌های کم‌فشار استاندارد ITF Red/Orange/Green\nتقویت مهارت‌های حرکتی و چابکی کودکان\nبرگزاری مسابقات درون‌آکادمی و اعطای گواهی\nمحیطی شاد، ایمن و کاملاً حرفه‌ای",
                is_active=True
            )
            TrainingClass.objects.create(
                title="کلاس‌های نیمه‌خصوصی (۲ الی ۴ نفره)",
                coach_name="مربیان رسمی فدراسیون تنیس",
                level="سطح متوسط و پیشرفته",
                duration="۱۰ جلسه ۱.۵ ساعته",
                tuition=3800000,
                schedule_info="روزهای فرد - ساعت ۱۸:۰۰ الی ۲۱:۰۰",
                features_list="تمرین‌های تاکتیکی دو به دو و گیم تاکتیک\nاصلاح راالی‌ها و ضربات انتهای زمین\nهزینه اقتصادی‌تر همراه با فضای شاد گروهی",
                is_active=True
            )

        # Generate Time Slots for Next 7 Days
        fa_days = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یکشنبه"]
        fa_months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
        
        today = datetime.now().date()
        times = [
            (time(8, 0), time(9, 30), 450000, 20),
            (time(9, 30), time(11, 0), 450000, 15),
            (time(11, 0), time(12, 30), 500000, 10),
            (time(14, 0), time(15, 30), 500000, 0),
            (time(15, 30), time(17, 0), 550000, 0),
            (time(17, 0), time(18, 30), 600000, 10),
            (time(18, 30), time(20, 0), 650000, 15),
            (time(20, 0), time(21, 30), 650000, 10),
            (time(21, 30), time(23, 0), 600000, 10),
        ]

        # Clear existing slots to generate fresh set
        CourtSlot.objects.all().delete()

        for day_offset in range(7):
            current_date = today + timedelta(days=day_offset)
            weekday_idx = current_date.weekday()
            day_name = fa_days[weekday_idx]
            
            # Simple Jalali date mock format for demo presentation
            # (e.g. شنبه ۱۵ اسفند)
            day_num = 10 + day_offset
            jalali_str = f"{day_name} {day_num} اسفند"
            if day_offset == 0:
                jalali_str = f"امروز ({day_name} {day_num} اسفند)"
            elif day_offset == 1:
                jalali_str = f"فردا ({day_name} {day_num} اسفند)"

            for court in [c1, c2]:
                for start_t, end_t, price, disc in times:
                    # Randomly mark a few slots as booked for realism
                    is_booked = False
                    if day_offset == 0 and start_t < time(15, 0):
                        is_booked = True
                    elif (day_offset + court.id) % 3 == 0 and start_t == time(18, 30):
                        is_booked = True

                    slot = CourtSlot.objects.create(
                        court=court,
                        date=current_date,
                        jalali_date=jalali_str,
                        start_time=start_t,
                        end_time=end_t,
                        price=price,
                        discount_percent=disc,
                        is_booked=is_booked
                    )
                    
                    if is_booked:
                        Reservation.objects.create(
                            slot=slot,
                            full_name="امیرحسین رضایی",
                            phone_number="09121112233",
                            tracking_code=f"RC-{10000 + slot.id}",
                            is_confirmed=True
                        )

        self.stdout.write(self.style.SUCCESS("Successfully seeded Royal Court database!"))
