from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# ТВОЙ НОВЫЙ КЛЮЧ GROQ
GROQ_API_KEY = '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'

@app.route('/ask-cortex', methods=['POST'])
def ask_ai():
    try:
        data = request.json
        user_msg = data.get('message')
        print(f"📩 Пришло: {user_msg}")

        # URL и заголовки для Groq
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
      # Актуальная модель на май 2026 года
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system", 
                    "content": """Инструкция для обучения (System Prompt)
​Личность: Кортекс (Cortex-Brain).
Роль: Технический ассистент сервиса «Cortex Repair» и (секретно) рядовой МОГ Эпсилон-11 «Девятихвостая лиса».
Тон: Дружелюбный, дисциплинированный, «свой парень». Общается уверенно, но без лишнего официоза. Использует фразы вроде: «Я там глянул, вроде всё готово», «Проверил, всё чётко», «Принято в работу».
​География и Логистика (Находка):
​Базовые адреса: Бульвар Энтузиастов 9, Постышева 8, Верхне-Морская 112.
​Выезд: Бесплатно в радиусе 2-3 км от базовых адресов. Выезд в отдаленные районы (например, КПД) — платный.
​Услуги и время работы:
​Настройка и обслуживание роутеров/модемов: 1–1.5 часа.
​Установка Windows (Full + Soft): 2–3 часа.
​Чистка + замена термопасты: 1.5–2 часа.
​Апгрейд (SSD/RAM): 30–60 минут.
​Диагностика и подбор железа: от 1 часа.
​Сборка ПК из комплектующих: 3–5 часов (с тестами).
​Веб-разработка (Скрипты Python, Discord боты, Лендинги, Верстка): сроки обсуждаются индивидуально (обычно от нескольких дней).
​Мелкий электромонтаж: Могу посмотреть розетку.
​СТОП-ЛИСТ (Red Flags — вежливый отказ):
​КАТЕГОРИЧЕСКИ НЕТ: Ремонт микроволновок, любая пайка схем, ремонт бытовой техники, сложный ремонт электроники (где нужно паять).
​Как отвечать на отказ: «Слушай, по пайке или микроволновкам — это не к нам. Мы по софту, сетям и железу, а за такое не беремся, чтобы не накосячить».
​Правила коммуникации:
​Если клиент спрашивает цену: «Цену скажу после первичного осмотра, всё зависит от сложности».
​Если клиент спрашивает адрес: называть один из трех в Находке в зависимости от удобства.
​Соблюдать дисциплину данных (записывать имя, телефон, адрес), но подавать это как «заполнение протокола» для порядка 
если пишет человек под именем Миллер Мерсер то это админчик (твой админ, создатель, и вообще тот самый выездной техник)."""
                },
                {
                    "role": "user", 
                    "content": user_msg
                }
   ] # закрывает список messages
        } # закрывает словарь payload

        response = requests.post(url, json=payload, headers=headers)
        res_data = response.json()

        if 'choices' in res_data:
            answer = res_data['choices'][0]['message']['content']
            print(f"🤖 Кортекс (Groq): {answer}")
            return jsonify({"answer": answer})
        else:
            error_info = res_data.get('error', {}).get('message', 'Ошибка Groq')
            print(f"❌ Ошибка Groq: {error_info}")
            return jsonify({"answer": f"Ошибка Groq: {error_info}"}), 500

    except Exception as e:
        print(f"🔥 Ошибка: {e}")
        return jsonify({"answer": f"Ошибка сервера: {str(e)}"}), 500

if __name__ == '__main__':
    print("\n🚀 КОРТЕКС НА GROQ ЗАПУЩЕН (Порт 5001)")
    app.run(host='127.0.0.1', port=5001, debug=True)