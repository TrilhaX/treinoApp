from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

treinos = {
    "Segunda": [
        "Supino reto com barra – 4x8-10",
        "Supino inclinado com halteres – 3x10",
        "Crossover na polia – 3x12",
        "Tríceps testa com barra EZ – 3x10",
        "Tríceps pulley – 3x12",
        "Mergulho entre bancos – 2x15"
    ],

    "Terca": [
        "Puxada alta (frente) – 4x10",
        "Remada curvada com barra – 3x8-10",
        "Remada unilateral com halteres – 3x10",
        "Rosca direta com barra – 3x10",
        "Rosca alternada com halteres – 3x10",
        "Rosca concentrada – 2x12"
    ],

    "Quarta": [
        "Agachamento livre – 4x10",
        "Leg press – 3x12",
        "Cadeira extensora – 3x15",
        "Cadeira flexora – 3x15",
        "Stiff com halteres – 3x12",
        "Elevação de pernas – 3x20",
        "Abdominal supra – 3x20"
    ],

    "Quinta": [
        "Desenvolvimento com halteres – 4x10",
        "Elevação lateral – 3x12",
        "Elevação frontal – 3x12",
        "Encolhimento com barra – 4x15",
        "Remada alta – 3x12"
    ],
    "Sexta": [
        "Supino reto – 3x10",
        "Agachamento – 3x12",
        "Puxada alta – 3x10",
        "Elevação lateral – 3x15",
        "Rosca direta – 3x12",
        "Tríceps corda – 3x12",
        "Abdominais (livre) – 3x20"
    ]
}
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=5, padding=10)

        for dia in treinos.keys():
            if dia == "Segunda":
                btn = Button(text=dia, size_hint=(1, 0.2), background_normal="./styles/img/peitoTreinoImagem.webp",)
            elif dia == "Terça":
                btn = Button(text=dia, size_hint=(1, 0.2), background_normal="./styles/img/peitoTreinoImagem.webp",)
            elif dia == "Quarta":
                btn = Button(text=dia, size_hint=(1, 0.2), background_normal="./styles/img/peitoTreinoImagem.webp",)
            elif dia == "Quinta":
                btn = Button(text=dia, size_hint=(1, 0.2), background_normal="./styles/img/peitoTreinoImagem.webp",)
            else:
                btn = Button(text=dia, size_hint=(1, 0.2), background_normal="./styles/img/peitoTreinoImagem.webp",)
            
            btn.bind(on_release=self.ir_para_treino)
            layout.add_widget(btn)

        self.add_widget(layout)

    def ir_para_treino(self, instance):
        self.manager.current = "treino"
        self.manager.get_screen("treino").mostrar_treinos(instance.text)

class TreinoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.add_widget(self.layout)

    def mostrar_treinos(self, dia):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=f"Treinos de {dia}", font_size=24, size_hint=(1, 0.2)))

        for exercicio in treinos[dia]:
            self.layout.add_widget(Label(text=f"- {exercicio}", font_size=18, size_hint=(1, 0.1)))

        voltar = Button(text="Voltar", size_hint=(1, 0.2))
        voltar.bind(on_release=self.voltar)
        self.layout.add_widget(voltar)

    def voltar(self, instance):
        self.manager.current = "menu"

class TreinoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(TreinoScreen(name="treino"))
        return sm

TreinoApp().run()