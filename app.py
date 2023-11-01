import tkinter as tk
import requests

# Chave da API OpenWeather (CONTA JOÃO VITOR)
api_key = "601016df9ac3a0db2d6228757bd661f0"

def obter_clima():
    cidade = cidade_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br" # link da API
    requisicao = requests.get(url)
    data = requisicao.json()

    if data["cod"] == 200:
        temperatura = data["main"]["temp"] - 273.15
        descricao = data["weather"][0]["description"]
        vento = data['wind']['speed']
        resultado_label.config(text=f"Temperatura: {temperatura: .1f}°C\nCondição: {descricao}\nVento: {vento} Km/h", fg='white')
        sugerir_esportes(descricao, vento, temperatura)
    else:
        resultado_label.config(text="Cidade não encontrada", fg='white')

def sugerir_esportes(condicao, vento, temperatura):
    condicao = condicao.lower()
    esportes_sugeridos = []

    # Sugestões com base na temperatura
    if temperatura < 10:
        esportes_sugeridos.append("Esqui, Esportes em áreas climatizadas")
    elif 10 <= temperatura <= 40 and "céu limpo" in condicao or "algumas nuvens" in condicao or "nuvens dispersas" in condicao or "nuvens quebradas" in condicao:
        esportes_sugeridos.append("Corrida, Ciclismo, Futebol")
    elif temperatura > 37:
        esportes_sugeridos.append("Natação, Esporte evitando exposição ao sol")

    # Se a temperatura for muito baixa, anular as outras sugestões
    if temperatura < 10:
        esportes_label.config(text="Sugestões de esportes para baixas temperaturas:\n" + "\n".join(esportes_sugeridos), fg='white')
    else:
        # Sugestões com base na descrição e no vento
        if "nublado" in condicao or "nuvens nubladas" in condicao or "trovoada com chuva fraca" in condicao or "trovoada com chuva" in condicao or "trovoada com chuva forte" in condicao or "chuva leve" in condicao or "chuva moderada" in condicao or "chuva muito forte" in condicao or "chuva forte" in condicao or "garoa leve" in condicao or "névoa" in condicao:
            esportes_sugeridos.append("Esporte em área coberta / fechada")

        if "neve" in condicao or "pouca neve" in condicao:
            esportes_sugeridos.append("Esqui ou Snowboard")

        if vento >= 7:  
            esportes_sugeridos.append("Vento bom para Kitesurf (Na presença de mar)")
        elif vento >= 10:
            esportes_sugeridos.append("Vento bom para Vela (Na presença de mar)")

        if esportes_sugeridos:
            esportes_label.config(text="Esportes sugeridos:\n" + "\n".join(esportes_sugeridos), fg='white')
        else:
            esportes_label.config(text="Sem sugestões de esportes neste clima", fg='white')


# Configurações da janela
janela = tk.Tk()
janela.title("SPORTS WEATHER")
janela.geometry('510x570')
janela.configure(bg='#181818')


fonte = ('Arial Rounded MT Bold', 14, 'bold')
    
titulo_label = tk.Label(janela, text="SPORTS WEATHER", font=('Helvetica', 20, 'bold', 'italic'), bg='#181818', fg='#33FFC2')
titulo_label.pack(pady=10)

# Inserir a cidade
cidade_label = tk.Label(janela, text="Digite o nome da cidade:", font=fonte, bg='#181818', fg='white', padx=10, pady=10)
cidade_label.pack()
cidade_entry = tk.Entry(janela, font=fonte)
cidade_entry.pack(padx=10, pady=5)

# Botão para obter o clima e os esportes
obter_clima_button = tk.Button(janela, text="Obter Informações", command=obter_clima, font=fonte, bg='#33FFC2', padx=10, pady=6)
obter_clima_button.pack(pady=7)

# Exibir o resultado clima
resultado_label = tk.Label(janela, text="", font=fonte, bg='#181818', fg='white', padx=10, pady=4)
resultado_label.pack(pady=6)

# Exibir sugestões de esportes
esportes_label = tk.Label(janela, text="", font=fonte, bg='#181818', fg='white', padx=10, pady=4)
esportes_label.pack(pady=2)

# Ícone do Aplicativo
icone_esportivo = tk.PhotoImage(file="icone_esportivo.png")
icone_label = tk.Label(janela, image=icone_esportivo, bg='#181818', padx=8, pady=0)
icone_label.pack(pady=0)

# Iniciar a janela
janela.mainloop()
