from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Note
import json

# Create your views here.



# task_list = [
#         {
#         "name": "A" ,
#         "note": "Lên kế hoạch tập thể dục",
#         },
#         {
#         "name": "B",
#         "note": "Đi học phát triển ứng dụng lúc 12h30 chiều thứ 4"
#         },
#         {
#         "name": "C"  ,
#         "note": "Thiết kế web giới thiệu bản thân ....."
#         },  
#         {
#             "name":"D", 
#             "note":"Thiết kế web giới thiệu bản thân .....",
#         }
#     ]


def home(request):

    task_list = Note.objects.all()
    return render(request, "mytodolist/home.html", {
        "task_list": task_list})


def update_note(request):
    
    if request.method == 'POST':
        
        data = json.loads(request.body)
        note_id = data.get('note_id')
        done = data.get('done')

        
        if note_id is None or done is None:
            return HttpResponse("Invalid data", status=400)

        # Lưu dữ liệu vào cơ sở dữ liệu
        try:
            note = Note.objects.get(id=note_id)
            note.done = done
            note.save()
            return HttpResponse("Note updated successfully")
        except Note.DoesNotExist:
            return HttpResponse("Note not found", status=404)
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}", status=500)
    else:
        return HttpResponse("Invalid request", status=405)

def post_task(request):
    
    if request.method == 'POST' :
        my_input = request.POST.get('my_input', None)
        if my_input:
            note_tmp = Note()
            note_tmp.content= my_input
            note_tmp.done = False
            note_tmp.save()

        return HttpResponseRedirect(reverse("home"))
        

        
  