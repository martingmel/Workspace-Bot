#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
بوت تليجرام لإنشاء المواقع - الملف الرئيسي
"""

import logging
from telegram.ext import Application
from config import BOT_TOKEN
from handlers import setup_handlers
import os

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def create_directories():
    """إنشاء المجلدات المطلوبة"""
    directories = ['websites', 'logs', 'data']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"تم إنشاء مجلد: {directory}")

def main():
    """تشغيل البوت"""
    try:
        # إنشاء المجلدات المطلوبة
        create_directories()
        
        # التحقق من وجود توكن البوت
        if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
            logger.error("❌ يرجى إضافة توكن البوت في ملف config.py")
            return
        
        # إنشاء التطبيق
        application = Application.builder().token(BOT_TOKEN).build()
        
        # إعداد المعالجات
        setup_handlers(application)
        
        # رسالة بدء التشغيل
        logger.info("🤖 بوت إنشاء المواقع يعمل الآن...")
        print("🤖 بوت إنشاء المواقع يعمل الآن...")
        print("📋 للإيقاف اضغط Ctrl+C")
        
        # تشغيل البوت
        application.run_polling(
            allowed_updates=['message', 'callback_query'],
            drop_pending_updates=True
        )
        
    except Exception as e:
        logger.error(f"خطأ في تشغيل البوت: {e}")
        print(f"❌ خطأ في تشغيل البوت: {e}")

if __name__ == '__main__':
    main()