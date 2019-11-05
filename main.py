import os
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ButtonsTemplate, TemplateSendMessage, MessageAction,
)


app = Flask(__name__)


#環境変数からLINE Access Tokenを設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
#環境変数からLINE Channel Secretを設定
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN) #アクセストークンを入れてください
handler = WebhookHandler(LINE_CHANNEL_SECRET) #Channel Secretを入れてください

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

    #テキストメッセージが送信されたときの処理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text

    if text == 'スタート':
        buttons_template = ButtonsTemplate(
            text='さぁ、冒険に出よう。', actions=[
                MessageAction(label='旧王都', text='2'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '2':
        buttons_template = ButtonsTemplate(
            text='ここはかつて、北部の帝国の侵攻で廃墟となった旧王都だ。今ではドラゴンやワイバーンが巣食う危険な場所と化している。目の前には廃墟がある。さて、君はどうしようかと足を止めた。', actions=[
                MessageAction(label='辺りを探索', text='3'),
                MessageAction(label='廃墟に入る', text='4'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '3':
        buttons_template = ButtonsTemplate(
            text='君は廃墟周辺の探索を始めた。遠くでワイバーンの鳴き声が聞こえる。', actions=[
                MessageAction(label='来た道を戻り廃墟に入る', text='4'),
                MessageAction(label='もう少し探す', text='5'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '4':
        buttons_template = ButtonsTemplate(
            text='とても静かだ。崩れた屋根から日差しが差し込む。', actions=[
                MessageAction(label='先へ進む', text='13'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '5':
        buttons_template = ButtonsTemplate(
            text='君は立ち止まり、廃墟の壁を眺めた。よく見ると隠し扉だ。罠かもしれない。', actions=[
                MessageAction(label='放っておこう', text='17'),
                MessageAction(label='隠し扉を開ける', text='16'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '6':
        buttons_template = ButtonsTemplate(
            text='小部屋に入るとそこには盗賊がいた。突然隠れ家に踏み込まれた盗賊は慌てたが、君に敵意がないと見ると、俺に用なら前金だと言ってふてぶてしく居直った。', actions=[
                MessageAction(label='お金を渡す', text='7'),
                MessageAction(label='お金を渡さない', text='8'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '7':
        buttons_template = ButtonsTemplate(
            text='この廃墟にはレッドドラゴンが巣食い、財宝の山を寝床にしているそうだ。君はその話について、もっと詳しく説明するよう盗賊に迫った。さて、君はどちらの道を選ぶ？', actions=[
                MessageAction(label='財宝の山を目指す', text='9'),
                MessageAction(label='迂回する', text='12'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '8':
        buttons_template = ButtonsTemplate(
            text='金がないなら帰りな。そう言って盗賊は出口を指差す', actions=[
                MessageAction(label='やっぱりお金を渡す', text='7'),
                MessageAction(label='大人しく帰る', text='18'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '9':
        buttons_template = ButtonsTemplate(
            text='盗賊は震えながら道を教えた。君はレッドドラゴンが眠る財宝の間へと向かう。', actions=[
                MessageAction(label='進む', text='10'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '10':
        buttons_template = ButtonsTemplate(
            text='あたりには硫黄の臭いが漂い、地鳴りようなイビキが聞こえる。覚悟を決めたら進みたまえ、レッドドラゴンはすぐそこだ。', actions=[
                MessageAction(label='進む', text='19'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '11':
        buttons_template = ButtonsTemplate(
            text='君はL字の曲がり角にきた。蝙蝠が君の来訪に警戒し飛び立つ。', actions=[
                MessageAction(label='南へ進む', text='14'),
                MessageAction(label='西へ進む', text='13'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '12':
        buttons_template = ButtonsTemplate(
            text='君は財宝の山を諦め、廃墟内の探索を続ける。どうやら、この廃墟には地下があるようだ。', actions=[
                MessageAction(label='進む', text='20'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '13':
        buttons_template = ButtonsTemplate(
            text='君はT字路に立っている。西に進むと入り口の方だ。東と南に進めるが、どちらも何者の気配もない。', actions=[
                MessageAction(label='南に進む', text='15'),
                MessageAction(label='東に進む', text='11'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '14':
        buttons_template = ButtonsTemplate(
            text='君はT字路に立っている。南から物音が聞こえた。誰かいるのか？', actions=[
                MessageAction(label='北へ進む', text='11'),
                MessageAction(label='南へ進む', text='6'),
                MessageAction(label='西へ進む', text='15'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '15':
        buttons_template = ButtonsTemplate(
            text='君はL字の曲がり角に立っている。いつ魔物が現れてもおかしくない。', actions=[
                MessageAction(label='北へ進む', text='13'),
                MessageAction(label='東へ進む', text='14'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '16':
        buttons_template = ButtonsTemplate(
            text='君は隠し扉を開け、廃墟に中に入っていった。以前に人が通った跡がある。', actions=[
                MessageAction(label='進む', text='6'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '17':
        buttons_template = ButtonsTemplate(
            text='この辺りには何もない。', actions=[
                MessageAction(label='来た道を戻り廃墟に入る', text='4'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '18':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='君は来た道を帰り、旧王都を後にした。何も得る事なく1日を終えた。END①変わらない日常'))

    elif text == '19':
        buttons_template = ButtonsTemplate(
            text='君が財宝の間へと足を踏み入れると、レッドドラゴンは目を覚まし建物が軋む程の唸り声を上げた。人間１人を丸呑みしてもおかしくない大きさだ。', actions=[
                MessageAction(label='戦う', text='36'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '20':
        buttons_template = ButtonsTemplate(
            text='じめじめしている。この地下はどこに続いているのだろう。しばらく進むとどうやら洞窟にたどり着いたようだ。', actions=[
                MessageAction(label='進む', text='21'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '21':
        buttons_template = ButtonsTemplate(
            text='洞窟の入り口に立っている。ランタンに火を灯し、君は先を急ぐ。', actions=[
                MessageAction(label='北へ進む', text='29'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '22':
        buttons_template = ButtonsTemplate(
            text='君は洞窟を抜けた。目の前にはワイバーンの巣が広がっている。ワイバーンは辺りに見当たらず、静かだ。', actions=[
                MessageAction(label='そのまま進み巣を抜ける', text='30'),
                MessageAction(label='卵を持ち帰ろう', text='31'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '23':
        buttons_template = ButtonsTemplate(
            text='君はL字の曲がり角に立っている。随分奥まできた。生きて帰れるだろうか。', actions=[
                MessageAction(label='北へ進む', text='25'),
                MessageAction(label='東へ進む', text='29'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '24':
        buttons_template = ButtonsTemplate(
            text='君はL字の曲がり角に立っている。蛇が君を襲ってきたが、君は腰に差しているナイフを素早く取り出し返り討ちにした。', actions=[
                MessageAction(label='南へ進む', text='29'),
                MessageAction(label='西へ進む', text='27'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '25':
        buttons_template = ButtonsTemplate(
            text='君はT字路に立っている。どこからか鳴き声が聞こえる。', actions=[
                MessageAction(label='北へ進む', text='27'),
                MessageAction(label='南へ進む', text='23'),
                MessageAction(label='西へ進む', text='26'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '26':
        buttons_template = ButtonsTemplate(
            text='君はL字の曲がり角にいる。北の方から光が差し込んでいる。', actions=[
                MessageAction(label='北へ進む', text='22'),
                MessageAction(label='東へ進む', text='25'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '27':
        buttons_template = ButtonsTemplate(
            text='君はL字の曲がり角に立っている。少し疲れた。', actions=[
                MessageAction(label='南へ進む', text='25'),
                MessageAction(label='東へ進む', text='24'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '28':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='君は洞窟を抜けることができた。頭上から日差しが差し込む。しかしそこには、ワイバーンの巣が広がっていた。君は卵を守るワイバーンに見つかってしまい、襲われた。END②ワイバーンに敗北'))

    elif text == '29':
        buttons_template = ButtonsTemplate(
            text='君は十字路に立っている。東の方から風を感じる。出口だろうか？', actions=[
                MessageAction(label='北へ進む', text='24'),
                MessageAction(label='南へ進む', text='21'),
                MessageAction(label='東へ進む', text='28'),
                MessageAction(label='西へ進む', text='23'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '30':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='30. 無事巣を抜け、地上に戻ってこれた。君は生きている事に感謝した。今日はもう帰ろう。END③生還'))

    elif text == '31':
        buttons_template = ButtonsTemplate(
            text='ワイバーンの卵は人間の赤ん坊と同じくらいの大きさだ。君はワイバーンの卵を一つ抱え、持ち帰る事にした。', actions=[
                MessageAction(label='ワイバーンだ！', text='32'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '32':
        buttons_template = ButtonsTemplate(
            text='ワイバーンに見つかってしまった。母親だろうか。こちらに敵意を示しており、非常に興奮している。耳障りな鳴き声が響く。しかし後には引けない。', actions=[
                MessageAction(label='走り抜ける', text='33'),
                MessageAction(label='剣を抜く', text='34'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '33':
        buttons_template = ButtonsTemplate(
            text='君は全速力で走り抜けることにした。ワイバーンは火を吹いたが間一髪で避け、逃げ切ることに成功した。', actions=[
                MessageAction(label='やった！逃げ切れたぞ！', text='35'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '34':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='君は勇敢にもワイバーンに戦いを挑んだ。しかしワイバーンは仲間を呼び、数え切れない数のワイバーンが空を舞う。END④絶望'))

    elif text == '35':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='35. 君は持ち帰ったワイバーンの卵を商人に売り、報酬を手に入れた。酒場で君は今回の冒険を自慢しながら酒を飲む。今度はどこへ行こうか。END⑤冒険を終えて'))

    elif text == '36':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡♡：赤竜♡♡♡】君はレッドドラゴンに', actions=[
                MessageAction(label='斬りかかる', text='37'),
                MessageAction(label='まずは様子を見る', text='40'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '37':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡♡：赤竜♡♡・】君はドラゴンの攻撃をかわしつつ近付き、高くジャンプしその背中を斬りつけた！鱗は硬いが確実に効いている。倒せない相手ではないと確信した。', actions=[
                MessageAction(label='一度距離を取る', text='38'),
                MessageAction(label='再び斬りかかる', text='41'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '38':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡♡：赤竜♡・・】君が距離を取るとレッドドラゴンは逃さまいと前足で君を踏みつけようとしてきた。君は寸前でそれを交わし、足にカウンターをお見舞いする。完全に君のペースだ。', actions=[
                MessageAction(label='一気に攻める', text='39'),
                MessageAction(label='再びカウンターを狙う', text='42'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '39':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡♡：赤竜・・・】ドラゴンは弱りつつある。君はこのチャンスを逃さまいとドラゴンの背後から背中に飛び移り心臓目掛けて剣を突き刺す。', actions=[
                MessageAction(label='…', text='45'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '40':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡・：赤竜♡♡♡】ドラゴンはこの場から立ち去れを言わんばかりに火を吹き、部屋が炎で包まれる。君は間一髪盾で直撃は防げたが、火傷を負ってしまった。', actions=[
                MessageAction(label='物陰に隠れる', text='51'),
                MessageAction(label='攻める', text='52'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '41':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡・：赤竜♡♡・】再び斬りかかろうとした次の瞬間には君は壁に打ち付けられていた。ドラゴンの尻尾で弾かれたようだ。全く見えなかったその攻撃に恐怖し君は足が震える。', actions=[
                MessageAction(label='カウンターを狙う', text='43'),
                MessageAction(label='正面から斬りかかる', text='49'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '42':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡・：赤竜♡・・】君は落ち着き、ドラゴンからの攻撃を待った。十分に時間の与えられたドラゴンは大きく息を吸い冒険者目掛けて火を吹いた。避け切れなかった君は火傷を負う。', actions=[
                MessageAction(label='距離を詰める', text='46'),
                MessageAction(label='物陰に隠れる', text='47'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '43':
        buttons_template = ButtonsTemplate(
            text='【冒険者・・：赤竜♡♡・】君は落ち着き、ドラゴンからの攻撃を待った。十分に時間の与えられたドラゴンは大きく息を吸い冒険者目掛けて火を吹いた。', actions=[
                MessageAction(label='…', text='44'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '44':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='盾で防ぎ切れなかった君は炎に焼かれ、その場で息絶えた。君の冒険はここで終わった。END⑥敗北'))

    elif text == '45':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='背中に剣の刺さったレッドドラゴンはその場に倒れた。おめでとう。君は最強と謳われるレッドドラゴンを打ち倒した。どんな流れ者であろうと君の名を軽んじる者はいまい。END⑦手に入れた栄光'))

    elif text == '46':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡・：赤竜・・・】ドラゴンは弱りつつある。君はこのチャンスを逃さまいと攻撃を躱しながら距離を詰め、ドラゴンの背後から背中に飛び移り心臓目掛けて剣を突き刺す。', actions=[
                MessageAction(label='…', text='45'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '47':
        buttons_template = ButtonsTemplate(
            text='【冒険者・・：赤竜♡・・】傷を負った君は物陰に隠れ、態勢を立て直すことにした。するとドラゴンはその場でジャンプをし、天井の一部が君の頭上目掛けて落ちてきた。', actions=[
                MessageAction(label='…', text='48'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '48':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='君は財宝と共に瓦礫に埋もれ、息絶えた。レッドドラゴンは飛び立ち、どこかへ去っていった。END⑧財宝と共に眠る'))

    elif text == '49':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡・：赤竜♡・・】正面から斬りかかる君にドラゴンは火の玉を吐いたが、盾で防がれた玉は軌道を変え壁に当たった。君は剣はドラゴンの腹部を斬り裂く。あと一歩だ。', actions=[
                MessageAction(label='一気に攻める', text='33'),
                MessageAction(label='ここは一旦落ち着こう', text='50'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '50':
        buttons_template = ButtonsTemplate(
            text='【冒険者・・：赤竜♡・・】君は落ち着き、ドラゴンからの攻撃を待った。十分に時間の与えられたドラゴンは大きく息を吸い冒険者目掛けて火を吹いた。', actions=[
                MessageAction(label='…', text='44'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '51':
        buttons_template = ButtonsTemplate(
            text='【冒険者・・：赤竜♡♡♡】傷を負った君は物陰に隠れ、態勢を立て直すことにした。するとドラゴンはその場でジャンプをし、天井の一部が君の頭上目掛けて落ちてきた。', actions=[
                MessageAction(label='…', text='48'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '52':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡・：赤竜♡♡・】防戦一方ではダメだ。君はドラゴンの攻撃をかわしつつ近付き、高くジャンプしその背中を斬りつけた！鱗は硬いが確実に効いている。倒せない相手ではないと確信した。', actions=[
                MessageAction(label='一気に攻める', text='53'),
                MessageAction(label='距離を取る', text='55'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '53':
        buttons_template = ButtonsTemplate(
            text='【冒険者・・：赤竜♡♡・】再び斬りかかろうとした次の瞬間には君は壁に打ち付けられていた。ドラゴンの尻尾で弾かれたようだ。', actions=[
                MessageAction(label='…', text='54'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '54':
        line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text='レッドドラゴンの最後の攻撃を君は目で追うこともできなかった。消えゆく意識の中、君はレッドドラゴンとの力の差に絶望していた。END⑨圧倒的敗北'))

    elif text == '55':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡・：赤竜♡・・】君が距離を取るとレッドドラゴンは逃さまいと前足で君を踏みつけようとしてきた。君は寸前でそれを交わし、足にカウンターをお見舞いする。完全に君のペースだ。', actions=[
                MessageAction(label='深呼吸する', text='56'),
                MessageAction(label='背後を取る', text='57'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '56':
        buttons_template = ButtonsTemplate(
            text='【冒険者・・：赤竜♡・・】君は深呼吸をし、落ち着いて次の一手を考えることにした。しかし十分に時間の与えられたドラゴンは大きく息を吸い冒険者目掛けて火を吹いた。', actions=[
                MessageAction(label='…', text='44'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    elif text == '57':
        buttons_template = ButtonsTemplate(
            text='【冒険者♡・：赤竜・・・】ドラゴンは弱りつつある。君はこのチャンスを逃さまいとドラゴンの背後から背中に飛び移り心臓目掛けて剣を突き刺す。', actions=[
                MessageAction(label='…', text='45'),
                ])
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(alt_text='linebotでゲームブック', template=buttons_template))

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='スタートと送信すると君の冒険が始まる'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host ='0.0.0.0',port = port)
