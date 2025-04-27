import openai
import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import NameGeneratorForm
from .models import GeneratedName

# OpenAI API võti
openai.api_key = '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'

# Parima nime soovitus
def suggest_best_name(keyword):
    names = GeneratedName.objects.all()
    best_name = None

    for name in names:
        name_text = name.name.lower()
        keyword_text = keyword.lower()

        if (keyword_text in name_text or name_text[:3] in name_text) and len(name_text) <= 12:
            best_name = name
            break

    if not best_name and names.exists():
        best_name = names.order_by('-created_at').first()

    return best_name

# Peamine vaade: nime genereerimine ja kuvamine
def generate_name(request):
    generated_names = None
    keyword = None

    if request.method == 'POST':
        form = NameGeneratorForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']

            # OpenAI päring
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Sa oled loominguline nimegeneraator."},
                    {"role": "user", "content": f"Paku 5 loomingulist nime märksõnale: {keyword}."}
                ]
            )
            generated_names = response['choices'][0]['message']['content']

            # Salvesta iga genereeritud nimi
            for line in generated_names.split('\n'):
                cleaned_name = line.strip('-•').strip()
                if cleaned_name:
                    GeneratedName.objects.create(keyword=keyword, name=cleaned_name)

    else:
        form = NameGeneratorForm()

    favorite_names = GeneratedName.objects.filter(is_favorite=True).order_by('-created_at')
    other_names = GeneratedName.objects.filter(is_favorite=False).order_by('-created_at')[:10]

    total_names = GeneratedName.objects.count()
    favorite_count = favorite_names.count()

    best_name = suggest_best_name(keyword) if keyword else None

    return render(request, 'generaator/generate_name.html', {
        'form': form,
        'generated_names': generated_names,
        'favorite_names': favorite_names,
        'other_names': other_names,
        'total_names': total_names,
        'favorite_count': favorite_count,
        'best_name': best_name,
    })

# Lemmikusse lisamine või eemaldamine
def toggle_favorite(request, name_id):
    name = get_object_or_404(GeneratedName, id=name_id)
    name.is_favorite = not name.is_favorite
    name.save()

    if name.is_favorite:
        messages.success(request, f'⭐ "{name.name}" lisatud lemmikutesse!')
    else:
        messages.success(request, f'❌ "{name.name}" eemaldatud lemmikutest!')

    return redirect('generate_name')

# Kõikide nimede kustutamine
def delete_all_names(request):
    GeneratedName.objects.all().delete()
    messages.success(request, "🗑️ Kõik nimed on edukalt kustutatud!")
    return redirect('generate_name')

# Laadi alla lemmiknimed TXT-failina
def download_favorites(request):
    favorite_names = GeneratedName.objects.filter(is_favorite=True).order_by('created_at')

    content = "Minu lemmiknimed:\n\n"
    for name in favorite_names:
        content += f"- {name.name} (märksõna: {name.keyword})\n"

    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="lemmik_nimed.txt"'
    return response

# Laadi alla lemmiknimed CSV-failina
def download_favorites_csv(request):
    favorite_names = GeneratedName.objects.filter(is_favorite=True).order_by('created_at')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lemmik_nimed.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nimi', 'Märksõna', 'Lisamise kuupäev'])

    for name in favorite_names:
        writer.writerow([name.name, name.keyword, name.created_at.strftime('%Y-%m-%d %H:%M')])

    return response
