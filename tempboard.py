import justpy as jp

def index():
    wp = jp.WebPage()
    
    # Linking stuff
    wp.head_html = '<link href="https://unpkg.com/nes.css/css/nes.css" rel="stylesheet" />'
    wp.css = '@import url(https://fonts.googleapis.com/css?family=Press+Start+2P);'
    wp.body_style = """background: url(https://raw.githubusercontent.com/StoicSun/Proto.Board/main/media/chess.webp);
    height: 100vh;
    position: relative;
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain; 
    """
    
    # Main div
    div = jp.Div(a=wp)

    # Heading
    head_div = jp.Div(classes="flex justify-center items-center", a=div)
    head_div1 = jp.Div(classes="flex justify-center", a=div)
    jp.H1(text="Proto.Board",
          classes="text-gray-700 pt-3 lg:pt-5 lg:pb-3 lg:m-auto lg:w-6 text-center lg:pr-48 text-2xl lg:text-3xl", a=head_div)
    jp.P(text="Temporary Solution",
         classes="text-gray-500 text-xs px-2 text-center md:text-left md:p-0 md:text-base", a=head_div1)
    head_div2 = jp.Div(classes="flex flex-center", a=head_div)
    jp.P(text="Source", classes="hidden text-gray-600 lg:text-xs lg:pt-5 lg:pr-1 lg:block", a=head_div2)
    github_link = jp.A(href="placeholder", target="_blank",
                       classes="hidden lg:pt-3 lg:block lg:ml-auto lg:pr-4", a=head_div2)
    jp.I(classes="nes-icon github", a=github_link)
    return wp

jp.justpy(index)