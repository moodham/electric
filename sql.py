import MySQLdb 

database1 = "hearsir2_electric"

user1 = ""
password1 = "spQvT:z#"

user1 = "11"
password1 = "1"

db = MySQLdb.connect(host="localhost", user=user1, password=password1, database=database1, charset='utf8', use_unicode=True)
x = (
    "علائم سیم کشی ساختمان",
    "موارد مقررات ملی ساختمان در سیم کشی",
    "نقش مقررات ملی ساختمان در سیم کشی",
    "ساختمانی بی نیاز از برق و گاز",
    "نحوه سیم کشی ساختمان",
    "روشهای تست و نگهداری کابلها و سیم ها",
    "ابزارات مورد نیاز سیم کشی ساختمان",
    "مدیریت هوشمند انرژی در ساختمان",
    "کلید دوپل",
    "دیمر برق",
    "انواع سیم های برق انتقال انرژی",
    "استاندارد برق ساختمان",
    "نقشه کشی برق",
    "بهينه سازي مصرف برق",
    "بانک خازن",
    "ایمنی ساختمانرعد و برق",
    "نرم افزار طراحی روشنایی",
    "اعلام حریق",
    "ساختار سیستم ارت در سیم کشی ساختمان",
    "دانلود نرم افزار مصرف برق ساختمان",
    "خدمات سیم کشی ساختمان",
    "انواع اتصالات ایفون",
    "انواع اتصلات ایفون",
    "انواع لامپ",
    "لامپ هالوژن",
    "نصب لامپ و روشنایی ساختمان",
    "لامپ و روشنایی",
    "انواع فيوز و نحوه حفاظت از مدارهاي الكتريكي",
    "تعمیرات تابلو برق های ساختمانی و صنعتی",
    "تابلو برق",
    "مراحل برق کشی ساختمان",
    "قیمت سیم کشی ساختمان",
    "نگهداری تاسیسات برق ساختمان",
    "اکیپ برقکار ساختمان",
    "سیم کشی تلفن سانترال پاناسونیک",
    "مشاوره سیم کشی ساختمان",
    "سیم کشی داکت کشی ساختمان",
    "امور برق کشی ساختمان",
    "لامپ و روشنایی ساختمان",
    "دوربین مدار بسته",
    "ایفون تصویری ساختمان",
    "سیم کشی پسیو و شبکه ساختمان",
    "سیم کشی برق اضطراری UPS",
    "نصب انواع سنسور",
    "نصب سنسور",
    "اموزش ایفون",
    "سیم کشی تو کار ساختمان",
    "اموزش نصب انتن مرکزی",
    "اموزش نصب روشنایی ساختمان",
    "برقکار ساختمان",
    "برق کشی آپارتمان",
    "دانلود اموزش سیم کشی ساختمان",
    "بروز ‌اتصالی برق در سیم‌کشی ساختمان سبب بروز آتش سوزی شد",
    "انتن",
    "اموزش برق کشی تلفن ساختمان",
    "آنتن مرکزی ساختمان",
    "استخدام برقکار ساختمان",
    "اموزش سیم کشی ساختمان",
    "اموزش نصب دزدگیر اماکن",
    "اموزش انتقال تصویر دوربین مداربسته",
    "ساخت روشنایی چراغ خواب",
    "سیم کشی رو کار ساختمان",
    "نگهداری برق ساختمان",
    "برق رسانی و تامین برق",
    "نصب تابلو برق های صنعتی",
    "سیم کشی برق ساختمان",
    "روشهای مختلف سیم کشی ساختمان",
    "نقشه کشی پریزهای برق ساختمان",
    "لوله کشی برق",
    "قوانین عالیه و نظارتی برق ساختمان",
    "مراحل برق کاری ساختمان",
    "ساختمان کابل های برق",
    "موتورهای الکتریکی",
    "سیم کشی هوشمند ساختمان",
    "سنسورهای هوشمند برق",
    "سیم کشی برق : چگونگی رساندن برق در حیاط",
    "فرز ترین ربات ربات پارکور کار",
    "فرز ترین ربات عمودی",
    "احداث 10800 مگاوات نیروگاه جدید",
    "استفاده از کابل های KNX در نقل و انتقالات مترو لندن",
    "لایحه برخورد با استفاده‌کنندگان غیرمجاز برق تصویب شد",
    "سرمایه گذاری ۱۰۰ میلیارد دلاری چین در انرژی بادی",
    "برق شهر لاس‌و‌گاس با انرژی سبز تامین می‌شود",
    "فوت سالانه 700 نفر به دلیل بی توجهی به مقررات ایمنی برق",
)
c = db.cursor()
for i in range(1, 85):

    print(len(x))
    print(i, x[i-1], type(x[i-1]))
    a=x[i-1]
    print(a)
    s=f"UPDATE blogs_posts SET post_title = '{a}'   WHERE id = {i};"
    print(s)
    c.execute(s)


c.close()

# print("****************************")

# max_price = 5
# c.execute(
#    """SELECT max(id) FROM blogs_posts group by post_title having count(*) > 1 ;"""
# )
# vv = c.fetchall()
# print(vv)
# print(type(vv))


# a=c.DictCursor()
# print(a)
# print(type(a))


# for i in r:
#    print(i)
