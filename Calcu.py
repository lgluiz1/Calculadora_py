import flet as ft



def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = ft.colors.BLACK
    page.window_width = 350
    page.window_height= 450
    page.window_min_width= 350
    page.window_min_height= 450

    result = ft.Text(value="0", height=30, color=ft.colors.WHITE, size=20)

    creditos = ft.Text(value=f"Projeto Desenvolvido Por Luiz Gustavo", color=ft.colors.WHITE)

    def limpar(l):
        result.value = "0"
        page.update()

    def numeros(event):
        valor_botao = event.control.text
        if valor_botao.isdigit():       
            if result.value == "0":
                result.value=""
            else:     
                result.value += valor_botao
                page.update()
                
        if valor_botao in ["+", "-", "*", "/", "%",".",""]:
            result.value += valor_botao
            page.update()
        if valor_botao == "=":
            resultado = eval(result.value)
            result.value = str(resultado)
            page.update()
    
    page.add(
        
        ft.Row(controls=[result] , alignment='end'),
        ft.Row(controls=[
            ft.ElevatedButton(text= "AC" , height=50, on_click=limpar),
            ft.ElevatedButton(text= "+/=", height=50, on_click=numeros),
            ft.ElevatedButton(text= "%", width=70, height=50, on_click=numeros),
            ft.ElevatedButton(text= "/", width=70, height=50 ,on_click=numeros),
            
        ]),
        ft.Row(controls=[
            ft.ElevatedButton(text= "7", width=70,height=50, on_click=numeros),
            ft.ElevatedButton(text= "8", width=70 ,height=50, on_click=numeros),
            ft.ElevatedButton(text= "9", width=70 ,height=50, on_click=numeros),
            ft.ElevatedButton(text= "*", width=70,height=50, on_click=numeros)
        ]),
        ft.Row(controls=[
            ft.ElevatedButton(text= "4", width=70,height=50, on_click=numeros),
            ft.ElevatedButton(text= "5", width=70,height=50, on_click=numeros),
            ft.ElevatedButton(text= "6", width=70,height=50, on_click=numeros),
            ft.ElevatedButton(text= "-", width=70,height=50, on_click=numeros)
        ]),
        ft.Row(controls=[
            ft.ElevatedButton(text= "1", width=70,height=50, on_click=numeros),
            ft.ElevatedButton(text= "2", width=70,height=50, on_click=numeros),
            ft.ElevatedButton(text= "3", width=70,height=50, on_click=numeros),
            ft.ElevatedButton(text= "+", width=70,height=50, on_click=numeros)
        ]),
        ft.Row(controls=[
            ft.ElevatedButton(text= "0", width=120,height=50, on_click=numeros),
            ft.ElevatedButton(text= ".", width=85,height=50, on_click=numeros),
            ft.ElevatedButton(text= "=", width=85,height=50, on_click=numeros)
        ]),
        ft.Row(controls=[creditos], alignment="Center")
    )

ft.app(target=main)