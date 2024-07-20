from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Conversation, Message
from .forms import MessageForm

@login_required
def conversation_list(request):
    conversations = Conversation.objects.filter(participants=request.user)
    return render(request, 'messaging/conversation_list.html', {'conversations': conversations})

@login_required
def conversation_detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    if request.user not in conversation.participants.all():
        return redirect('conversation_list')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.conversation = conversation
            message.save()
            return redirect('conversation_detail', pk=conversation.pk)
    else:
        form = MessageForm()

    return render(request, 'messaging/conversation_detail.html', {'conversation': conversation, 'form': form})

@login_required
def start_conversation(request, user_id):
    other_user = get_object_or_404(User, pk=user_id)
    if other_user == request.user:
        return redirect('conversation_list')

    # Check if a conversation already exists
    conversation = Conversation.objects.filter(participants=request.user).filter(participants=other_user).first()
    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user)
        conversation.participants.add(other_user)
    
    return redirect('conversation_detail', pk=conversation.pk)