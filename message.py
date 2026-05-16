"""
Multi-Language Messages Module
Professional messaging for the Quantum Crypto bot with advanced HTML formatting
"""

LANGUAGES = {
    "en": "🇬🇧 English",
    "ru": "🇷🇺 Русский",
    "hi": "🇮🇳 हिन्दी",
    "ar": "🇸🇦 العربية",
    "zh": "🇨🇳 中文",
    "ja": "🇯🇵 日本語",
    "it": "🇮🇹 Italiano",
    "pt": "🇧🇷 Português",
}

MESSAGES = {
    "en": {
        # Intro
        "welcome": (
            "<blockquote><b>✦ QUANTUM TOKEN PRO ✦</b></blockquote>\n\n"
            "<b>Get latest news About tokens and blockchain world!✨</b>\n\n"
            "Get real-time market data, institutional insights, and precision conversion tools instantly.\n\n<i>Powered by CoinGecko APIs</i>"
        ),
        "choose_language": (
            "<blockquote><b>🌍 SYSTEM LANGUAGE SETUP</b></blockquote>\n\n"
            "<i>Please select your preferred operational language below:</i>"
        ),
        "language_saved": (
            "<blockquote><b>✅ PREFERENCE SAVED</b></blockquote>\n\n"
            "<i>Your interface language has been successfully updated.</i>"
        ),
        
        # Main Menu
        "main_menu": (
            "<blockquote><b>❖ MAIN DASHBOARD</b></blockquote>\n\n"
            "<b>📊 Live Market</b> <code>—</code> <i>Track top digital assets</i>\n"
            "<b>📰 Global News</b> <code>—</code> <i>Real-time market intelligence</i>\n"
            "<b>🔁 Exchange Hub</b> <code>—</code> <i>High-precision swap engine</i>\n"
            "<b>⚙️ Parameters</b> <code>—</code> <i>System configuration</i>\n\n"
            "<i>Awaiting your command...</i>"
        ),
        
        # Buttons
        "prices_button": "📊 Live Market",
        "news_button": "📰 News Feed",
        "converter_button": "🔁 Convert Hub",
        "settings_button": "⚙️ Parameters",
        "help_button": "❓ System Help",
        "back_button": "⬅️ Return",
        "refresh_button": "🔄 Sync Data",
        "home_button": "🏠 Dashboard",
        
        # Prices
        "prices_title": (
            "<blockquote><b>📊 MARKET WATCH</b></blockquote>\n\n"
            "<i>Select an asset to view real-time metrics and 24-hour momentum.</i>"
        ),
        "coin_detail_header": "<blockquote><b>{emoji} {name} ({symbol})</b></blockquote>",
        "price_label": "❖ <b>Spot Price:</b>",
        "change_label": "❖ <b>24h Delta:</b>",
        "high_label": "📈 <b>24h Peak:</b>",
        "low_label": "📉 <b>24h Floor:</b>",
        "market_cap_label": "🌍 <b>Valuation:</b>",
        "volume_label": "💸 <b>Volume:</b>",
        "source_label": "<pre>⚡ Data stream verified via CoinGecko API</pre>",
        
        # Chart
        "generating_chart": (
            "<blockquote><b>📊 COMPILING ANALYTICS...</b></blockquote>\n"
            "<i>Rendering 24-hour visual momentum matrix. Please stand by.</i>"
        ),
        "chart_ready": "<blockquote><b>📈 TECHNICAL CHART ACQUIRED</b></blockquote>",
        "chart_error": (
            "<blockquote><b>⚠️ SYSTEM ALERT</b></blockquote>\n\n"
            "<i>Visualization engine temporarily offline. Retrying connection...</i>"
        ),
        
        # News
        "news_prompt": (
            "<blockquote><b>📰 INTELLIGENCE FEED</b></blockquote>\n\n"
            "<i>Activate push notifications for critical market shifts and global headlines.</i>\n\n"
            "Initialize alerts?"
        ),
        "news_enabled": (
            "<blockquote><b>✅ ALERTS ACTIVE</b></blockquote>\n\n"
            "<i>Monitoring global feeds. You will be notified of major market events.</i>"
        ),
        "news_disabled": (
            "<blockquote><b>🔕 ALERTS SUSPENDED</b></blockquote>\n\n"
            "<i>Manual interface access required for news updates.</i>"
        ),
        "fetching_news": (
            "<blockquote><b>⏳ ACCESSING DATABANKS...</b></blockquote>\n"
            "<i>Syncing latest geopolitical and market intelligence.</i>"
        ),
        "news_unavailable": (
            "<blockquote><b>⚠️ FEED DISCONNECTED</b></blockquote>\n\n"
            "<i>Unable to establish secure link with news servers.</i>"
        ),
        "latest_news": "<blockquote><b>📰 GLOBAL MARKET INTELLIGENCE</b></blockquote>",
        "news_item": "✦ <a href=\"{link}\"><b>{title}</b></a>",
        "no_news": (
            "<blockquote><b>📭 NO NEW REPORTS</b></blockquote>\n\n"
            "<i>The intelligence feed is currently dormant.</i>"
        ),
        
        # Converter
        "converter_title": (
            "<blockquote><b>🔁 EXCHANGE ENGINE</b></blockquote>\n\n"
            "<i>Initialize high-precision fiat and digital asset conversion.</i>"
        ),
        "select_coin": (
            "<blockquote><b>🪙 PHASE 1: ASSET SELECTION</b></blockquote>\n\n"
            "<i>Designate the primary asset for conversion.</i>"
        ),
        "select_type": (
            "<blockquote><b>💱 PHASE 2: TARGET CLASSIFICATION</b></blockquote>\n\n"
            "<i>Select destination asset class (Fiat Reserve or Digital Asset).</i>"
        ),
        "select_target": (
            "<blockquote><b>💵 PHASE 3: DESTINATION ASSET</b></blockquote>\n\n"
            "<i>Designate specific target currency.</i>"
        ),
        "enter_amount": (
            "<blockquote><b>✍️ PHASE 4: QUANTITY</b></blockquote>\n\n"
            "<i>Specify the volume of <b>{coin}</b> to process.</i>\n\n"
            "<pre>Awaiting numeric input...</pre>"
        ),
        
        # Conversion buttons
        "to_fiat_button": "💵 Fiat Reserve",
        "to_crypto_button": "🪙 Digital Asset",
        
        # Conversion results
        "conversion_result": (
            "<blockquote><b>✅ TRANSACTION CALCULATED</b></blockquote>\n\n"
            "<pre>{amount} {coin_symbol}\n"
            "   ⋮\n"
            "{result} {target_symbol}</pre>\n\n"
            "<i>Rate synchronized via local memory cache.</i>"
        ),
        "invalid_amount": (
            "<blockquote><b>⚠️ SYNTAX ERROR</b></blockquote>\n\n"
            "<i>Invalid volume specified. Please input a positive numeric value.</i>"
        ),
        "conversion_error": (
            "<blockquote><b>❌ PROCESSING FAILURE</b></blockquote>\n\n"
            "<i>Market data sync incomplete. Please reset and try again.</i>"
        ),
        
        # Settings
        "settings_title": (
            "<blockquote><b>⚙️ SYSTEM PREFERENCES</b></blockquote>\n\n"
            "<i>Configure operational parameters and interface settings.</i>"
        ),
        "language_button": "🌍 Regional Settings",
        "news_toggle_button": "🔔 Push Alerts",
        "news_status": "<blockquote><b>🔔 ALERTS STATUS:</b> {status}</blockquote>",
        "on": "<code>[ ACTIVE ]</code>",
        "off": "<code>[ OFFLINE ]</code>",
        
        # Errors
        "error_timeout": (
            "<blockquote><b>⏱️ LATENCY EXCEEDED</b></blockquote>\n\n"
            "<i>Server response timeframe breached. Connection severed.</i>"
        ),
        "error_connection": (
            "<blockquote><b>🌐 UPLINK FAILED</b></blockquote>\n\n"
            "<i>Unable to establish secure connection to external APIs.</i>"
        ),
        "error_generic": (
            "<blockquote><b>❌ CRITICAL ERROR</b></blockquote>\n\n"
            "<i>An unexpected anomaly occurred within the system.</i>"
        ),
        
        # Status messages
        "typing": "typing",
        "uploading": "uploading photo",
    },
    
        "ru": {
        "welcome": (
            "<blockquote><b>✦ QUANTUM TOKEN PRO ✦</b></blockquote>\n\n"
            "Ваш элитный командный центр. Мгновенный доступ к рыночным данным, аналитике и инструментам точной конвертации."
        ),
        "choose_language": (
            "<blockquote><b>🌍 ЯЗЫК СИСТЕМЫ</b></blockquote>\n\n"
            "<i>Выберите предпочитаемый язык интерфейса:</i>"
        ),
        "language_saved": (
            "<blockquote><b>✅ НАСТРОЙКИ СОХРАНЕНЫ</b></blockquote>\n\n"
            "<i>Язык интерфейса успешно обновлен.</i>"
        ),
        "main_menu": (
            "<blockquote><b>❖ ГЛАВНАЯ ПАНЕЛЬ</b></blockquote>\n\n"
            "<b>📊 Рынок онлайн</b> <code>—</code> <i>Отслеживание активов</i>\n"
            "<b>📰 Лента новостей</b> <code>—</code> <i>Глобальная аналитика</i>\n"
            "<b>🔁 Обменник</b> <code>—</code> <i>Система конвертации</i>\n"
            "<b>⚙️ Параметры</b> <code>—</code> <i>Настройки системы</i>\n\n"
            "<i>Ожидание команды...</i>"
        ),
        "prices_button": "📊 Рынок онлайн",
        "news_button": "📰 Лента новостей",
        "converter_button": "🔁 Обменник",
        "settings_button": "⚙️ Параметры",
        "help_button": "❓ Справка",
        "back_button": "⬅️ Возврат",
        "refresh_button": "🔄 Синхронизация",
        "home_button": "🏠 Панель",
        "prices_title": (
            "<blockquote><b>📊 ОБЗОР РЫНКА</b></blockquote>\n\n"
            "<i>Выберите актив для просмотра метрик и динамики за 24ч.</i>"
        ),
        "coin_detail_header": "<blockquote><b>{emoji} {name} ({symbol})</b></blockquote>",
        "price_label": "❖ <b>Текущая цена:</b>",
        "change_label": "❖ <b>Дельта (24ч):</b>",
        "high_label": "📈 <b>Пик (24ч):</b>",
        "low_label": "📉 <b>Минимум (24ч):</b>",
        "market_cap_label": "🌍 <b>Капитализация:</b>",
        "volume_label": "💸 <b>Объём (24ч):</b>",
        "source_label": "<pre>⚡ Данные верифицированы через CoinGecko API</pre>",
        "generating_chart": (
            "<blockquote><b>📊 КОМПИЛЯЦИЯ АНАЛИТИКИ...</b></blockquote>\n"
            "<i>Отрисовка визуальной матрицы. Пожалуйста, подождите.</i>"
        ),
        "chart_ready": "<blockquote><b>📈 ТЕХНИЧЕСКИЙ ГРАФИК ПОЛУЧЕН</b></blockquote>",
        "chart_error": (
            "<blockquote><b>⚠️ СИСТЕМНОЕ ПРЕДУПРЕЖДЕНИЕ</b></blockquote>\n\n"
            "<i>Подсистема визуализации недоступна. Повторная попытка...</i>"
        ),
        "news_prompt": (
            "<blockquote><b>📰 ИНФОРМАЦИОННАЯ ЛЕНТА</b></blockquote>\n\n"
            "<i>Активировать push-уведомления о критических изменениях рынка?</i>"
        ),
        "news_enabled": (
            "<blockquote><b>✅ УВЕДОМЛЕНИЯ АКТИВНЫ</b></blockquote>\n\n"
            "<i>Мониторинг запущен. Вы будете получать оповещения.</i>"
        ),
        "news_disabled": (
            "<blockquote><b>🔕 УВЕДОМЛЕНИЯ ПРИОСТАНОВЛЕНЫ</b></blockquote>\n\n"
            "<i>Требуется ручной запрос для обновления новостей.</i>"
        ),
        "fetching_news": (
            "<blockquote><b>⏳ ОБРАЩЕНИЕ К БАЗАМ ДАННЫХ...</b></blockquote>\n"
            "<i>Синхронизация рыночной разведки.</i>"
        ),
        "news_unavailable": (
            "<blockquote><b>⚠️ СВЯЗЬ ПРЕРВАНА</b></blockquote>\n\n"
            "<i>Невозможно установить соединение с серверами новостей.</i>"
        ),
        "latest_news": "<blockquote><b>📰 ГЛОБАЛЬНАЯ АНАЛИТИКА РЫНКА</b></blockquote>",
        "converter_title": (
            "<blockquote><b>🔁 СИСТЕМА КОНВЕРТАЦИИ</b></blockquote>\n\n"
            "<i>Инициализация точного расчета курсов активов.</i>"
        ),
        "select_coin": (
            "<blockquote><b>🪙 ЭТАП 1: ВЫБОР АКТИВА</b></blockquote>\n\n"
            "<i>Укажите исходный актив для транзакции.</i>"
        ),
        "select_type": (
            "<blockquote><b>💱 ЭТАП 2: КЛАССИФИКАЦИЯ</b></blockquote>\n\n"
            "<i>Выберите целевой класс (Фиатный резерв или Цифровой актив).</i>"
        ),
        "select_target": (
            "<blockquote><b>💵 ЭТАП 3: ЦЕЛЕВОЙ АКТИВ</b></blockquote>\n\n"
            "<i>Укажите конкретную валюту назначения.</i>"
        ),
        "enter_amount": (
            "<blockquote><b>✍️ ЭТАП 4: ОБЪЁМ</b></blockquote>\n\n"
            "<i>Укажите количество <b>{coin}</b> для обработки.</i>\n\n"
            "<pre>Ожидание числового ввода...</pre>"
        ),
        "to_fiat_button": "💵 Фиатный резерв",
        "to_crypto_button": "🪙 Цифровой актив",
        "conversion_result": (
            "<blockquote><b>✅ РАСЧЕТ ЗАВЕРШЕН</b></blockquote>\n\n"
            "<pre>{amount} {coin_symbol}\n"
            "   ⋮\n"
            "{result} {target_symbol}</pre>\n\n"
            "<i>Курс синхронизирован через локальный кэш.</i>"
        ),
        "invalid_amount": (
            "<blockquote><b>⚠️ ОШИБКА СИНТАКСИСА</b></blockquote>\n\n"
            "<i>Недопустимый объем. Введите положительное число.</i>"
        ),
        "conversion_error": (
            "<blockquote><b>❌ СБОЙ ПРОЦЕССА</b></blockquote>\n\n"
            "<i>Данные рынка не синхронизированы. Повторите попытку.</i>"
        ),
        "settings_title": (
            "<blockquote><b>⚙️ ПАРАМЕТРЫ СИСТЕМЫ</b></blockquote>\n\n"
            "<i>Конфигурация рабочих параметров системы.</i>"
        ),
        "language_button": "🌍 Языковые настройки",
        "news_toggle_button": "🔔 Push-уведомления",
        "news_status": "<blockquote><b>🔔 СТАТУС УВЕДОМЛЕНИЙ:</b> {status}</blockquote>",
        "on": "<code>[ АКТИВНО ]</code>",
        "off": "<code>[ ОТКЛЮЧЕНО ]</code>",
        "error_timeout": "<blockquote><b>⏱️ ПРЕВЫШЕН ЛИМИТ ВРЕМЕНИ</b></blockquote>",
        "error_connection": "<blockquote><b>🌐 ОШИБКА СОЕДИНЕНИЯ</b></blockquote>",
        "error_generic": "<blockquote><b>❌ КРИТИЧЕСКАЯ ОШИБКА</b></blockquote>",
    },
    
    "hi": {
        "welcome": "<blockquote><b>✦ QUANTUM TOKEN PRO ✦</b></blockquote>\n\nआपका प्रोफेशनल टोकन कमांड सेंटर।",
        "choose_language": "<blockquote><b>🌍 भाषा सेटिंग्स</b></blockquote>\n\n<i>अपनी भाषा चुनें:</i>",
        "language_saved": "<blockquote><b>✅ सेटिंग्स अपडेटेड</b></blockquote>\n\n<i>भाषा सफलतापूर्वक सहेजी गई।</i>",
        "main_menu": "<blockquote><b>❖ मुख्य डैशबोर्ड</b></blockquote>\n\n<b>📊 लाइव कीमतें</b>\n<b>📰 बाज़ार समाचार</b>\n<b>🔁 एक्सचेंज हब</b>\n<b>⚙️ सिस्टम सेटिंग्स</b>",
        "prices_button": "📊 लाइव कीमतें",
        "news_button": "📰 समाचार फीड",
        "converter_button": "🔁 एक्सचेंज हब",
        "settings_button": "⚙️ सेटिंग्स",
        "help_button": "❓ सहायता",
        "back_button": "⬅️ पीछे जाएँ",
    },
    
    "zh": {
        "welcome": "<blockquote><b>✦ QUANTUM TOKEN PRO ✦</b></blockquote>\n\n欢迎使用您的专业代币指挥中心。",
        "choose_language": "<blockquote><b>🌍 系统语言设置</b></blockquote>\n\n<i>请选择您的首选操作语言：</i>",
        "language_saved": "<blockquote><b>✅ 偏好已保存</b></blockquote>\n\n<i>您的界面语言已成功更新。</i>",
        "main_menu": "<blockquote><b>❖ 主控制台</b></blockquote>\n\n<b>📊 实时市场</b>\n<b>📰 全球新闻</b>\n<b>🔁 兑换引擎</b>\n<b>⚙️ 系统参数</b>",
        "prices_button": "📊 实时市场",
        "news_button": "📰 新闻资讯",
        "converter_button": "🔁 兑换引擎",
        "settings_button": "⚙️ 系统参数",
        "help_button": "❓ 系统帮助",
        "back_button": "⬅️ 返回",
    },
    
    "ja": {
        "welcome": "<blockquote><b>✦ QUANTUM TOKEN PRO ✦</b></blockquote>\n\nプロフェッショナルなトークンコマンドセンターへようこそ。",
        "choose_language": "<blockquote><b>🌍 言語設定</b></blockquote>\n\n<i>希望する言語を選択してください:</i>",
        "language_saved": "<blockquote><b>✅ 設定完了</b></blockquote>\n\n<i>言語設定が更新されました。</i>",
        "main_menu": "<blockquote><b>❖ メインダッシュボード</b></blockquote>\n\n<b>📊 ライブマーケット</b>\n<b>📰 グローバルニュース</b>\n<b>🔁 為替ハブ</b>\n<b>⚙️ システム設定</b>",
        "prices_button": "📊 ライブマーケット",
        "news_button": "📰 ニュースフィード",
        "converter_button": "🔁 為替ハブ",
        "settings_button": "⚙️ 設定",
        "help_button": "❓ ヘルプ",
        "back_button": "⬅️ 戻る",
    },
}


def get_message(lang: str, key: str, **kwargs) -> str:
    """
    Get translated message with variable substitution
    
    Args:
        lang: Language code (e.g., 'en', 'ru')
        key: Message key
        **kwargs: Variables for formatting
    
    Returns:
        Translated and formatted message
    """
    
    # Fallback to English if language not found
    messages = MESSAGES.get(lang, MESSAGES["en"])
    message = messages.get(key, MESSAGES["en"].get(key, f"[{key}]"))
    
    # Format with provided kwargs
    try:
        return message.format(**kwargs) if kwargs else message
    except KeyError as e:
        return f"[Missing: {e}]"


def get_language_name(lang_code: str) -> str:
    """Get display name for language code"""
    return LANGUAGES.get(lang_code, lang_code)
