from django import forms;

class ContactoForm(forms.Form):
    #TIPO_CONSULTA=(
      #  ('','-seleccione-'),
        #(1,'ejemplo1'),
        #(2,'ejemplo2'),
        #(3,'ejemplo3'),
   # ) ejemplo de un campo select
    nombre=forms.CharField(label='nombre')
    email=forms.EmailField(label='email',max_length=50)
    asunto=forms.CharField(label='asunto')
    mensaje=forms.CharField(label='mensaje', max_length=250, required=False)
    #tipo_consulta=forms.ChoiceField(label='elija una opccion', choices=TIPO_CONSULTA)me muestra el select
    #check=forms.BooleanField(label='ejemplo de un check', required=False)