import justpy as jp
from html_comps import input_table_html
from score_data import enter_row, return_row, delete_scores

scores = [0]*7
players = {1:'Simi',2:'Suraj',3:'Abhi',4:'Piyush',5:'Ashish',6:'Nitu',7:'Parle'}
wp = jp.WebPage(delete_flag=False)
wp.title = 'ProtoBoard'
wp.favicon = 'media/favicon.svg'

# Linking stuff
wp.head_html = '''<link href="https://unpkg.com/nes.css/css/nes.css" rel="stylesheet" />
<script>confirm = () => true;</script>
'''
wp.css = '@import url(https://fonts.googleapis.com/css?family=Press+Start+2P);'
wp.body_style = """
background-image: url(https://raw.githubusercontent.com/StoicSun/Proto.Board/main/media/chess.png);
height: 100vh;
position: relative;
background-position: center;
background-repeat: no-repeat;
background-size: contain; 
"""

# Main div
content = jp.Div(classes='flex flex-col h-screen justify-between', a=wp)
div = jp.Div(classes="mb-auto", a=content)

# Heading
head_div = jp.Div(classes="flex justify-center items-center", a=div)
head_div1 = jp.Div(classes="flex justify-center items-center", a=div)
jp.H1(text="Proto.Scoreboard",
        classes="text-center text-gray-700 pt-3 lg:pt-5 lg:pb-3 text-center text-xl lg:text-3xl", a=head_div)
jp.P(text="Temporary Solution",
        classes="text-center text-gray-600 text-xs text-center md:p-0 md:text-base", a=head_div1)
jp.Img(src="https://www.svgrepo.com/show/83116/board-games-set.svg", classes="h-16 w-20", a=jp.Div(classes="flex justify-center mt-4 -mb-16", a=div))

# Body 
board = jp.parse_html(input_table_html,a=jp.Div(classes="flex justify-center -ml-24", a=div))
session_data = board.name_dict['i-score']

def update_board(self,msg):
        delete_scores()
        self.text = 'Click twice to update'
        for j in range(7):
                enter_row(players[session_data[j].id],session_data[j].value)
        sorted_scores = return_row()
        if len(sorted_scores) >= 3:
                self.first.text = f'First:{sorted_scores[-1]}'
                self.sec.text = f'Second:{sorted_scores[-2]}'
                self.third.text = f'Third:{sorted_scores[-3]}'
                self.poke_div.show = not self.poke_div.show

sub_btn = jp.Button(text="Current Standings",classes="nes-btn is-primary",a=jp.Div(classes="flex justify-center mt-8",a=div),click=update_board)
poke_div = jp.Div(classes="flex flex-col justify-center mt-3", show= False, a=div)
charm_div = jp.Div(classes="flex flex-row justify-center items-center", a=poke_div)
jp.Img(src="https://raw.githubusercontent.com/PMDCollab/SpriteCollab/master/portrait/0004/Joyous.png", classes="w-10 h-10 mr-2",a=charm_div)
first = jp.P(text="First:",classes="text-center text-xl pt-5", a=charm_div)
frok_div = jp.Div(classes="flex flex-row justify-center items-center", a=poke_div)
jp.Img(src="https://raw.githubusercontent.com/PMDCollab/SpriteCollab/master/portrait/0656/Stunned.png", classes="w-10 h-10 mr-2",a=frok_div)
sec = jp.P(text="Second:",classes="text-center text-xl pt-3", a=frok_div)
treecko_div = jp.Div(classes="flex flex-row justify-center items-center", a=poke_div)
jp.Img(src="https://raw.githubusercontent.com/PMDCollab/SpriteCollab/master/portrait/0252/Crying.png", classes="w-10 h-10 mr-2",a=treecko_div)
third = jp.P(text="Third:",classes="text-center text-xl pt-3", a=treecko_div)
sub_btn.poke_div = poke_div
sub_btn.first = first
sub_btn.sec = sec
sub_btn.third = third

# Footer
link_div = jp.Div(classes="flex justify-center", a=content)
jp.P(text='©2020 Suraj Das', classes='pt-1', a=link_div)
github_link = jp.A(classes='pb-2 px-3', href="https://github.com/StoicSun/Proto.Board", target="_blank", a=link_div)
jp.I(classes="nes-icon github", a=github_link)


def joint_edit():
    return wp

app = jp.app
jp.justpy(joint_edit, start_server=False)  
