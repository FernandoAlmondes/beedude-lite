from .models import Mapa, Node, Edge

from django import forms

#class formAddMapa(forms.Form):
#    nome = forms.CharField(label='Digite o nome do mapa', required=True, max_length=200)

class formAddMapa(forms.ModelForm):
    class Meta:
        model = Mapa
        fields = ['nome', 'servidor', 'default']
        labels = {'nome': 'Nome do mapa'}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'servidor': forms.Select(attrs={'class': 'form-control'}),
            'default': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class formAddNode(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['nome', 'label_template', 'icone', 'classe', 'mapa']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            "label_template": forms.Textarea(attrs={
                "class": "form-control",
                'style': 'height: 130px;',
                "placeholder": "Ex: Bits: {{1234}} {{lastvalue}} {{bps}}"
            }),
            'icone': forms.Select(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'mapa': forms.Select(attrs={'class': 'form-control'})
            }

class formAddEdge(forms.ModelForm):
    class Meta:
        model = Edge
        fields = ['nome', 'label_template', 'source', 'target', 'mapa']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            "label_template": forms.Textarea(attrs={
                "class": "form-control",
                'style': 'height: 130px;',
                "placeholder": "Ex: Bits: {{1234}} {{lastvalue}} {{bps}}"
            }),
            'source': forms.Select(attrs={'class': 'form-control'}),
            'target': forms.Select(attrs={'class': 'form-control'}),
            'mapa': forms.Select(attrs={'class': 'form-control'})
            }