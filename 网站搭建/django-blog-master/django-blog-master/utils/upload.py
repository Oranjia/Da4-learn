import os
import uuid
from django.views.decorators.csrf import csrf_exempt  # 取消csrftoken
from django.http import JsonResponse  # 返回json格式的数据
from django.conf import settings      # 配置文件


@csrf_exempt
def upload_file(request):

    # 获取表单上传的图片
    upload = request.FILES.get('upload')
    # 返回uid
    uid = ''.join(str(uuid.uuid4()).split('-'))
    # 修改图片名称
    # asdasd.jpg  fddg.png  ['sasda', 'jpg']
    names = str(upload.name).split('.')
    names[0] = uid
    # 返回修改过的图片格式
    upload.name = '.'.join(names)
    
    new_path = os.path.join(settings.MEDIA_ROOT, 'upload/', upload.name) 
    # 上传图片
    with open(new_path, 'wb+') as file:
        for chunk in upload.chunks():
            file.write(chunk)
    
    # 构造要求的数据格式并返回
    filename = upload.name
    url = '/media/upload/' + filename
    retdata = { 'url': url, 
                'uploaded': '1',
                'fileName': filename }
    return JsonResponse(retdata)