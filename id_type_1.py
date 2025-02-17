from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Словарь для хранения заявок
applications = {}

def add_application(update: Update, context: CallbackContext) -> None:

    """Добавляет новую заявку с ID пользователя."""

    user_id = update.effective_user.id
    username = update.effective_user.username or update.effective_user.full_name
    applications[user_id] = {'username': username, 'status': 'pending'}
    update.message.reply_text(f'Заявка добавлена для {username}.')

def change_application_id(update: Update, context: CallbackContext) -> None:

    """Изменяет ID пользователя на его имя или тег."""

    user_id = update.effective_user.id
    if user_id in applications:
        username = applications[user_id]['username']
        # Удаляем заявку с ID и добавляем с именем пользователя
        applications[username] = applications.pop(user_id)
        update.message.reply_text(f'ID изменен на {username}.')
    else:
        update.message.reply_text('Заявка не найдена.')
