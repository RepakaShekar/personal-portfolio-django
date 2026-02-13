from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-white/10 border border-white/20 rounded-lg px-4 py-3 text-white placeholder-gray-400 focus:outline-none focus:border-indigo-400 focus:ring-1 focus:ring-indigo-400 transition',
                'placeholder': 'Your name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-white/10 border border-white/20 rounded-lg px-4 py-3 text-white placeholder-gray-400 focus:outline-none focus:border-indigo-400 focus:ring-1 focus:ring-indigo-400 transition',
                'placeholder': 'your@email.com'
            }),

            'message': forms.Textarea(attrs={
                'class': 'w-full bg-white/10 border border-white/20 rounded-lg px-4 py-3 text-white placeholder-gray-400 focus:outline-none focus:border-indigo-400 focus:ring-1 focus:ring-indigo-400 transition',
                'rows': 4,
                'placeholder': 'Tell me about your project...'
            }),
        }