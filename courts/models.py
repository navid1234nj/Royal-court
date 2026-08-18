from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="Royal Court", verbose_name="نام مجموعه")
    site_title_fa = models.CharField(max_length=150, default="مجموعه تنیس رویال کورت", verbose_name="عنوان فارسی وبسایت")
    manager_name = models.CharField(max_length=100, default="محمد عتبات", verbose_name="نام مدیریت")
    phone_number = models.CharField(max_length=50, default="021-22001122 | 09121112233", verbose_name="شماره تماس پشتیبانی")
    instagram = models.CharField(max_length=100, default="@royalcourt_tennis", verbose_name="آیدی اینستاگرام")
    address = models.CharField(max_length=255, default="تهران، خیابان فرشته، مجموعه تنیس VIP رویال کورت", verbose_name="آدرس مجموعه")

    # Navigation labels
    nav_home = models.CharField(max_length=50, default="صفحه اصلی", verbose_name="متن منو: صفحه اصلی")
    nav_schedule = models.CharField(max_length=50, default="رزرو آنلاین سانس", verbose_name="متن منو: رزرو آنلاین")
    nav_classes = models.CharField(max_length=50, default="کلاس‌های آموزشی", verbose_name="متن منو: کلاس‌های آموزشی")
    nav_gallery = models.CharField(max_length=50, default="گالری تصاویر", verbose_name="متن منو: گالری تصاویر")
    nav_about = models.CharField(max_length=50, default="درباره ما", verbose_name="متن منو: درباره ما")

    # Hero section
    hero_tag = models.CharField(max_length=150, default="Royal Court | زمین استانداردهای بین‌المللی ITF", verbose_name="تگ هیرو")
    hero_title = models.CharField(max_length=200, default="تجربه‌ای متفاوت در لوکس‌ترین زمین تنیس خاکی", verbose_name="تیتر اصلی هیرو")
    hero_subtitle = models.TextField(default="زمین تنیس خاکی استاندارد با زیرسازی تخصصی، نورپردازی شبانه، مربیان بین‌المللی و رزرو آنلاین آنی بدون نیاز به ثبت‌نام", verbose_name="توضیحات هیرو")
    hero_btn1 = models.CharField(max_length=100, default="رزرو فوری سانس‌های امروز", verbose_name="متن دکمه رزرو هیرو")
    hero_btn2 = models.CharField(max_length=100, default="ثبت‌نام کلاس آموزشی", verbose_name="متن دکمه کلاس هیرو")
    hero_stat1_num = models.CharField(max_length=50, default="۱ زمین", verbose_name="آمار ۱ (عدد/عنوان)")
    hero_stat1_label = models.CharField(max_length=100, default="خاکی سرخ بین‌المللی", verbose_name="آمار ۱ (توضیح)")
    hero_stat2_num = models.CharField(max_length=50, default="۲۴ / ۷", verbose_name="آمار ۲ (عدد/عنوان)")
    hero_stat2_label = models.CharField(max_length=100, default="رزرو آنلاین آنی بدون ورود", verbose_name="آمار ۲ (توضیح)")
    hero_stat3_num = models.CharField(max_length=50, default="VIP", verbose_name="آمار ۳ (عدد/عنوان)")
    hero_stat3_label = models.CharField(max_length=100, default="نور شب، کلاب‌هاوس و پارک", verbose_name="آمار ۳ (توضیح)")
    hero_image = models.ImageField(upload_to="hero/", blank=True, null=True, verbose_name="تصویر اصلی هیرو")

    # Schedule section
    schedule_tag = models.CharField(max_length=150, default="برنامه زمانی و رزرو مستقیم", verbose_name="تگ بخش تقویم")
    schedule_title = models.CharField(max_length=200, default="تقویم سانس‌های آزاد و رزرو آنلاین", verbose_name="عنوان بخش تقویم")
    schedule_subtitle = models.TextField(default="روز و ساعت مورد نظر خود را انتخاب کرده و بدون نیاز به ورود، با وارد کردن نام و شماره تماس رزرو کنید.", verbose_name="زیرعنوان تقویم")
    base_session_price = models.PositiveIntegerField(default=500000, verbose_name="قیمت پایه هر سانس (تومان)")
    default_discount_percent = models.PositiveIntegerField(default=15, verbose_name="درصد تخفیف عمومی (%)")
    price_notice_text = models.CharField(max_length=255, default="⚡ تخفیف ۱۵ درصدی برای تمامی سانس‌های صبحگاهی و آخر هفته به مدت محدود!", verbose_name="متن اطلاع‌رسانی بالای تقویم")
    reservation_warning_title = models.CharField(max_length=150, default="هشدار مهم رزرو:", verbose_name="تیتر هشدار رزرو")
    reservation_warning_text = models.TextField(default="سانس ثبت شده نهایی بوده و طبق قوانین مجموعه غیرقابل تغییر، لغو یا استرداد وجه می‌باشد. لطفاً قبل از تایید نهایی از ساعت و روز رزرو اطمینان حاصل فرمایید.", verbose_name="متن هشدار رزرو")

    # Classes section
    classes_tag = models.CharField(max_length=150, default="آکادمی تخصصی تنیس", verbose_name="تگ بخش کلاس‌ها")
    classes_title = models.CharField(max_length=200, default="کلاس‌های آموزشی، آکادمی کودکان و شهریه", verbose_name="عنوان بخش کلاس‌ها")
    classes_subtitle = models.TextField(default="زیر نظر مستقیم استاد و سرمربیان رسمی فدراسیون تنیس جمهوری اسلامی ایران", verbose_name="زیرعنوان بخش کلاس‌ها")

    # Gallery section
    gallery_tag = models.CharField(max_length=150, default="تصاویر مجموعه", verbose_name="تگ گالری")
    gallery_title = models.CharField(max_length=200, default="گالری تصاویر و نمای زمین خاکی", verbose_name="عنوان گالری")
    gallery_subtitle = models.TextField(default="نمای دید شبانه، فضا و کیفیت زمین مدرن رویال کورت", verbose_name="زیرعنوان گالری")

    # About section
    about_tag = models.CharField(max_length=150, default="درباره مجموعه", verbose_name="تگ درباره ما")
    about_title = models.CharField(max_length=200, default="درباره آکادمی و مجموعه تنیس رویال کورت", verbose_name="عنوان درباره ما")
    about_text = models.TextField(default="مجموعه ورزشی رویال کورت با مدیریت جناب آقای محمد عتبات، با بهره‌گیری از مدرن‌ترین استانداردهای بین‌المللی فدراسیون جهانی تنیس (ITF)، مجهز به زمین خاکی سرخ استاندارد، سیستم نورپردازی حرفه‌ای دید در شب، کلاب‌هاوس VIP، و کادر آموزشی مجرب آماده خدمت‌رسانی به علاقه‌مندان تنیس می‌باشد.", verbose_name="متن درباره ما")
    about_image = models.ImageField(upload_to="about/", blank=True, null=True, verbose_name="تصویر درباره ما")
    about_feature1_title = models.CharField(max_length=100, default="زیرسازی استاندارد ITF", verbose_name="ویژگی ۱ درباره ما (عنوان)")
    about_feature1_desc = models.CharField(max_length=150, default="زهکشی و خاک سرخ درجه یک", verbose_name="ویژگی ۱ درباره ما (توضیح)")
    about_feature2_title = models.CharField(max_length=100, default="نورپردازی شبانه LED", verbose_name="ویژگی ۲ درباره ما (عنوان)")
    about_feature2_desc = models.CharField(max_length=150, default="امکان بازی تا پاسی از شب", verbose_name="ویژگی ۲ درباره ما (توضیح)")
    about_feature3_title = models.CharField(max_length=100, default="پارکینگ اختصاصی", verbose_name="ویژگی ۳ درباره ما (عنوان)")
    about_feature3_desc = models.CharField(max_length=150, default="همراه با نگهبانی ۲۴ ساعته", verbose_name="ویژگی ۳ درباره ما (توضیح)")
    about_feature4_title = models.CharField(max_length=100, default="کافه و کلاب‌هاوس", verbose_name="ویژگی ۴ درباره ما (عنوان)")
    about_feature4_desc = models.CharField(max_length=150, default="سرو نوشیدنی‌های ورزشی", verbose_name="ویژگی ۴ درباره ما (توضیح)")

    # Footer
    footer_desc = models.CharField(max_length=255, default="مجموعه تخصصی تنیس خاکی رویال کورت - ارائه دهنده خدمات رزرو آنلاین و آموزش تنیس", verbose_name="متن توضیحات فوتر")
    footer_copyright = models.CharField(max_length=255, default="کلیه حقوق مادی و معنوی متعلق به مجموعه تنیس Royal Court می‌باشد.", verbose_name="متن کپی‌رایت فوتر")

    class Meta:
        verbose_name = "تنظیمات عمومی وبسایت"
        verbose_name_plural = "تنظیمات عمومی وبسایت"

    def __str__(self):
        return f"تنظیمات {self.site_name}"


class HeroSlide(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان اسلاید")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="زیرعنوان اسلاید")
    image = models.ImageField(upload_to="slides/", verbose_name="تصویر اسلاید")
    order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "اسلاید هیرو"
        verbose_name_plural = "اسلایدهای هیرو"
        ordering = ['order']

    def __str__(self):
        return self.title


class TennisCourt(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام زمین")
    court_type = models.CharField(max_length=100, default="تنیس خاکی (Red Clay)", verbose_name="نوع زمین")
    description = models.TextField(blank=True, verbose_name="توضیحات زمین")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "زمین تنیس"
        verbose_name_plural = "زمین‌های تنیس"

    def __str__(self):
        return self.name


class CourtSlot(models.Model):
    court = models.ForeignKey(TennisCourt, on_delete=models.CASCADE, related_name="slots", verbose_name="زمین تنیس")
    date = models.DateField(verbose_name="تاریخ (میلادی)")
    jalali_date = models.CharField(max_length=50, verbose_name="تاریخ شمسی", help_text="مانند: ۱۴۰۳/۱۲/۱۵ یا شنبه ۱۵ اسفند")
    start_time = models.TimeField(verbose_name="ساعت شروع")
    end_time = models.TimeField(verbose_name="ساعت پایان")
    price = models.PositiveIntegerField(verbose_name="قیمت سانس (تومان)")
    discount_percent = models.PositiveIntegerField(default=0, verbose_name="تخفیف (%)")
    is_booked = models.BooleanField(default=False, verbose_name="رزرو شده")
    is_blocked = models.BooleanField(default=False, verbose_name="مسدود توسط ادمین")

    class Meta:
        verbose_name = "سانس تقویم"
        verbose_name_plural = "سانس‌های تقویم"
        ordering = ['date', 'start_time']

    @property
    def final_price(self):
        if self.discount_percent > 0:
            return int(self.price * (1 - self.discount_percent / 100))
        return self.price

    def __str__(self):
        return f"{self.court.name} - {self.jalali_date} ({self.start_time.strftime('%H:%M')} تا {self.end_time.strftime('%H:%M')})"


class Reservation(models.Model):
    slot = models.OneToOneField(CourtSlot, on_delete=models.CASCADE, related_name="reservation", verbose_name="سانس رزرو شده")
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی رزرو کننده")
    phone_number = models.CharField(max_length=20, verbose_name="شماره تماس")
    tracking_code = models.CharField(max_length=20, unique=True, verbose_name="کد پیگیری رزرو")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت رزرو")
    is_confirmed = models.BooleanField(default=True, verbose_name="تایید شده")

    class Meta:
        verbose_name = "رزرو کاربر"
        verbose_name_plural = "لیست رزروها"
        ordering = ['-created_at']

    def __str__(self):
        return f"رزرو {self.full_name} - {self.slot}"


class GalleryCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان دسته‌بندی")

    class Meta:
        verbose_name = "دسته‌بندی گالری"
        verbose_name_plural = "دسته‌بندی‌های گالری"

    def __str__(self):
        return self.title


class GalleryItem(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان تصویر")
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="دسته‌بندی")
    image = models.ImageField(upload_to="gallery/", verbose_name="تصویر")
    description = models.CharField(max_length=255, blank=True, verbose_name="توضیح کوتاه")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "تصویر گالری"
        verbose_name_plural = "گالری تصاویر"

    def __str__(self):
        return self.title


class TrainingClass(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان کلاس آموزشی")
    coach_name = models.CharField(max_length=100, verbose_name="نام مدرس / سرمربی")
    level = models.CharField(max_length=100, default="مبتدی تا پیشرفته", verbose_name="سطح برگزاری")
    duration = models.CharField(max_length=100, default="۱۰ جلسه ۱ ساعته", verbose_name="مدت دوره")
    tuition = models.PositiveIntegerField(verbose_name="شهریه دوره (تومان)")
    schedule_info = models.CharField(max_length=200, default="روزهای زوج و فرد - هماهنگی با ادمین", verbose_name="زمان‌بندی کلاس")
    features_list = models.TextField(help_text="هر ویژگی در یک خط جدید وارد شود", verbose_name="ویژگی‌های کلاس")
    image = models.ImageField(upload_to="classes/", blank=True, null=True, verbose_name="تصویر کلاس")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "کلاس آموزشی"
        verbose_name_plural = "کلاس‌های آموزشی"

    def __str__(self):
        return self.title


class ClassEnrollment(models.Model):
    training_class = models.ForeignKey(TrainingClass, on_delete=models.CASCADE, related_name="enrollments", verbose_name="کلاس آموزشی")
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    phone_number = models.CharField(max_length=20, verbose_name="شماره تماس")
    notes = models.TextField(blank=True, verbose_name="توضیحات تکمیلی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت‌نام")

    class Meta:
        verbose_name = "ثبت‌نام کلاس آموزشی"
        verbose_name_plural = "ثبت‌نام‌های کلاس‌های آموزشی"

    def __str__(self):
        return f"{self.full_name} - {self.training_class.title}"

