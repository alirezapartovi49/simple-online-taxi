<template>
  <div class="support-container">
    <h4 class="mb-4">پشتیبانی</h4>

    <div class="card support-card mb-4">
      <div class="card-body">
        <div class="d-flex align-items-center">
          <div
            class="support-icon bg-primary text-white rounded-circle d-flex align-items-center justify-content-center"
          >
            <i class="fas fa-headphones fa-lg"></i>
          </div>
          <div class="ms-3">
            <h5 class="mb-0">تماس با پشتیبانی</h5>
            <p class="mb-0 text-muted">۰۲۱-۱۲۳۴۵۶۷۸</p>
          </div>
        </div>
      </div>
    </div>

    <div class="card support-card mb-4">
      <div class="card-body">
        <div class="d-flex align-items-center">
          <div
            class="support-icon bg-success text-white rounded-circle d-flex align-items-center justify-content-center"
          >
            <i class="fas fa-envelope fa-lg"></i>
          </div>
          <div class="ms-3">
            <h5 class="mb-0">ایمیل پشتیبانی</h5>
            <p class="mb-0 text-muted">support@taxiapp.com</p>
          </div>
        </div>
      </div>
    </div>

    <div class="card support-card">
      <div class="card-body">
        <h5 class="card-title mb-3">سوالات متداول</h5>

        <div v-for="(faq, index) in faqs" :key="index" class="faq-item mb-3">
          <div class="faq-question fw-bold mb-1">{{ faq.question }}</div>
          <div class="faq-answer text-muted">{{ faq.answer }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SupportView",
  setup() {
    const faqs = [
      {
        question: "چگونه می‌توانم سفر جدیدی را رزرو کنم؟",
        answer:
          "برای رزرو سفر جدید، به صفحه خانه بروید، محل شروع و مقصد سفر خود را وارد کنید، نوع خودرو را انتخاب کنید و دکمه 'درخواست سفر' را بزنید.",
      },
      {
        question: "چگونه می‌توانم وضعیت سفر خود را پیگیری کنم؟",
        answer:
          "بعد از درخواست سفر، به صفحه 'سفرهای من' بروید و روی سفر مورد نظر خود کلیک کنید تا وضعیت آن را مشاهده کنید.",
      },
      {
        question: "چگونه می‌توانم کیف پول خود را شارژ کنم؟",
        answer:
          "برای شارژ کیف پول، به قسمت پروفایل بروید و گزینه 'افزایش موجودی' را انتخاب کنید.",
      },
      {
        question: "چگونه می‌توانم با راننده تماس بگیرم؟",
        answer:
          "در صفحه پیگیری سفر، یک دکمه تماس با راننده وجود دارد که می‌توانید از طریق آن با راننده تماس بگیرید.",
      },
    ];

    return {
      faqs,
    };
  },
};
</script>

<style scoped>
.support-container {
  padding: 1rem;
}

.support-card {
  border-radius: 1rem;
}

.support-icon {
  width: 40px;
  height: 40px;
}

.faq-item {
  border-bottom: 1px solid #eee;
  padding-bottom: 0.5rem;
}

.faq-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}
</style>
