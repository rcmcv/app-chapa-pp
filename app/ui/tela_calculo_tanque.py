import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers import controller_materiais
import math

def area_tronco_cone(d_maior, d_menor, h_cone):
    R = d_maior / 2
    r = d_menor / 2
    g = math.sqrt((R - r)**2 + h_cone**2)
    return math.pi * (R + r) * g  # área lateral do tronco de cone (mm²)

def calcular_area_total_tanque(d, h, fundo_tipo, tampa_tipo, fd_menor=None, fh_cone=None, td_menor=None, th_cone=None):
    PI = math.pi
    r = d / 2
    area_lateral = PI * d * h

    # Fundo
    fundo_area = 0
    if fundo_tipo == "Plano":
        fundo_area = PI * r**2
    elif fundo_tipo == "Cônico" and fd_menor and fh_cone:
        fundo_area = area_tronco_cone(d, fd_menor, fh_cone)

    # Tampa
    tampa_area = 0
    if tampa_tipo == "Plano":
        tampa_area = PI * r**2
    elif tampa_tipo == "Cônico" and td_menor and th_cone:
        tampa_area = area_tronco_cone(d, td_menor, th_cone)

    return area_lateral + fundo_area + tampa_area  # resultado em mm²

def calcular_volume_m3(d, h, fundo_tipo, tampa_tipo, fd_menor=None, fh_cone=None, td_menor=None, th_cone=None):
    PI = math.pi
    r = d / 2 / 1000  # raio maior em metros
    h_m = h / 1000    # altura do cilindro em metros

    # Volume do cilindro (corpo principal)
    volume_cilindro = PI * r ** 2 * h_m

    # Volume do fundo cônico (tronco de cone)
    volume_fundo = 0
    if fundo_tipo == "Cônico" and fd_menor and fh_cone:
        R = d / 2 / 1000
        r_f = fd_menor / 2 / 1000
        h_f = fh_cone / 1000
        volume_fundo = (1/3) * PI * h_f * (R**2 + R*r_f + r_f**2)

    # Volume da tampa cônica (tronco de cone)
    volume_tampa = 0
    if tampa_tipo == "Cônico" and td_menor and th_cone:
        R = d / 2 / 1000
        r_t = td_menor / 2 / 1000
        h_t = th_cone / 1000
        volume_tampa = (1/3) * PI * h_t * (R**2 + R*r_t + r_t**2)

    # Volume total
    return volume_cilindro + volume_fundo + volume_tampa

def calcular_qtd_chapas(area_total_mm2):
    chapas = controller_materiais.listar_chapas()
    if not chapas:
        raise Exception("Nenhuma chapa cadastrada.")
    chapa = chapas[0]
    area_chapa = chapa[2] * chapa[3]
    qtd = math.ceil(area_total_mm2 / area_chapa)
    sobra = (qtd * area_chapa) - area_total_mm2
    return qtd, sobra, area_chapa

def abrir_tela_calculo_tanque(dados_edicao=None):
    janela = tk.Toplevel()
    janela.title("Cálculo de Tanques")
    janela.geometry("600x640")
    janela.resizable(False, False)

    # Formulário
    frame = ttk.LabelFrame(janela, text="Dados do Tanque")
    frame.pack(fill="x", padx=10, pady=10)

    tipo_tanque = ttk.Combobox(frame, values=["Redondo"], state="readonly")
    tipo_tanque.set("Redondo")
    entrada_cliente = ttk.Entry(frame)
    entrada_diametro = ttk.Entry(frame)
    entrada_altura = ttk.Entry(frame)

    fundo_tipo = ttk.Combobox(frame, values=["Plano", "Cônico"], state="readonly")
    fundo_tipo.set("Plano")
    entrada_f_dmenor = ttk.Entry(frame)
    entrada_f_altura = ttk.Entry(frame)

    tampa_tipo = ttk.Combobox(frame, values=["Nenhuma", "Plano", "Cônico"], state="readonly")
    tampa_tipo.set("Nenhuma")
    entrada_t_dmenor = ttk.Entry(frame)
    entrada_t_altura = ttk.Entry(frame)

    campos = [
        ("Tipo de Tanque", tipo_tanque),
        ("Cliente", entrada_cliente),
        ("Diâmetro (mm)", entrada_diametro),
        ("Altura (mm)", entrada_altura),
        ("Tipo de Fundo", fundo_tipo),
        ("Ø Menor Fundo (mm)", entrada_f_dmenor),
        ("Altura Cone Fundo (mm)", entrada_f_altura),
        ("Tipo de Tampa", tampa_tipo),
        ("Ø Menor Tampa (mm)", entrada_t_dmenor),
        ("Altura Cone Tampa (mm)", entrada_t_altura)
    ]

    for i, (label, widget) in enumerate(campos):
        ttk.Label(frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=2)
        widget.grid(row=i, column=1, padx=5, pady=2)

    def toggle_campos_conicos(*args):
        estado_f = "normal" if fundo_tipo.get() == "Cônico" else "disabled"
        estado_t = "normal" if tampa_tipo.get() == "Cônico" else "disabled"
        entrada_f_dmenor.configure(state=estado_f)
        entrada_f_altura.configure(state=estado_f)
        entrada_t_dmenor.configure(state=estado_t)
        entrada_t_altura.configure(state=estado_t)

    fundo_tipo.bind("<<ComboboxSelected>>", toggle_campos_conicos)
    tampa_tipo.bind("<<ComboboxSelected>>", toggle_campos_conicos)
    toggle_campos_conicos()

    # Resultados
    resultado_frame = ttk.LabelFrame(janela, text="Resultados do Cálculo")
    resultado_frame.pack(fill="x", padx=10, pady=10)

    resultado_area = tk.StringVar()
    resultado_volume = tk.StringVar()
    resultado_chapas = tk.StringVar()
    resultado_sobra = tk.StringVar()

    ttk.Label(resultado_frame, text="Área Total (m²):").grid(row=0, column=0, sticky="w", padx=5, pady=2)
    ttk.Label(resultado_frame, textvariable=resultado_area).grid(row=0, column=1, sticky="w")
    ttk.Label(resultado_frame, text="Volume (m³):").grid(row=1, column=0, sticky="w", padx=5, pady=2)
    ttk.Label(resultado_frame, textvariable=resultado_volume).grid(row=1, column=1, sticky="w")
    ttk.Label(resultado_frame, text="Qtd Chapas:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
    ttk.Label(resultado_frame, textvariable=resultado_chapas).grid(row=2, column=1, sticky="w")
    ttk.Label(resultado_frame, text="Sobra (m²):").grid(row=3, column=0, sticky="w", padx=5, pady=2)
    ttk.Label(resultado_frame, textvariable=resultado_sobra).grid(row=3, column=1, sticky="w")

    def calcular():
        try:
            d = float(entrada_diametro.get().replace(",", "."))
            h = float(entrada_altura.get().replace(",", "."))
            fd_menor = float(entrada_f_dmenor.get()) if fundo_tipo.get() == "Cônico" else None
            fh_cone = float(entrada_f_altura.get()) if fundo_tipo.get() == "Cônico" else None
            td_menor = float(entrada_t_dmenor.get()) if tampa_tipo.get() == "Cônico" else None
            th_cone = float(entrada_t_altura.get()) if tampa_tipo.get() == "Cônico" else None

            area_total = calcular_area_total_tanque(d, h, fundo_tipo.get(), tampa_tipo.get(), fd_menor, fh_cone, td_menor, th_cone)
            volume = calcular_volume_m3(d, h, fundo_tipo.get(), tampa_tipo.get(), fd_menor, fh_cone, td_menor, th_cone)
            chapas, sobra, _ = calcular_qtd_chapas(area_total)

            resultado_area.set(f"{area_total / 1e6:.2f}")
            resultado_volume.set(f"{volume:.3f}")
            resultado_chapas.set(str(chapas))
            resultado_sobra.set(f"{sobra / 1e6:.2f}")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    ttk.Button(janela, text="Calcular", command=calcular).pack(pady=10)
