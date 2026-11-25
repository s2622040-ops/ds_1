import flet as ft


def main(page: ft.Page):

    # Hello World
    hello_world = ft.Text("Hello World", size=50)

    # カウンター表示用のオブジェクト
    counter = ft.Text("0", size=50, data=0)

    # +ボタンがクリックされた時に呼び出される関数
    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    # +ボタンを描画エリアに追加
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )

    # -ボタンがクリックされた時に呼び出される関数
    def decreased_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data -= 1
        counter.value = str(counter.data)

    # コンテンツを描画エリアに表示
    page.add(
        # 実行環境に表示エリアを合わせるためのオブジェクト
        ft.SafeArea(
            expand=True,
            # パーツをまとめるオブジェクト
            content=ft.Container(
                # content=counter,
                content = ft.Column(controls = [hello_world, counter], alignment=ft.MainAxisAlignment.CENTER),
                alignment=ft.Alignment.CENTER,
            ),
        ),
        # マイナスボタンを左下に配置
        ft.FloatingActionButton(icon=ft.Icons.REMOVE, key="decreased", on_click=decreased_click)
    )


if __name__ == "__main__":
    ft.run(main)
