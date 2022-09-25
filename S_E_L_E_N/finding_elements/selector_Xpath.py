
# lepiej tag niż *

# //tag[@attribute='value']

# //*[@id='navbar']
# //div[@id='navbar']
# //div[@class='homepage-hero']//a[text()='Enroll now']
# //div[@id='navbar']//a[text()='Login'] - nie zadziała bo białe znaki
# //div[@id='navbar']//a[contains(text(), 'Login')] - zastępujemy contains
# //div[@id='navbar']//a[contains(@class, 'navbar-link')]
# //div[@id='navbar']//a[contains(@class, 'navbar-link') and contains(@href, 'sign-in')]

# starts-with
# jak u góry szukamy link do login
# //div[@id='navbar']//a[start-with(@class,'navbar-link')]
# //div[@id='navbar']//a[@href='/sign-in']
# //a[@href='/sign-in']

# Parents - przed/po 
# xpath-to-some-element//parent::<tag>      rodzic
# xpath-to-some-element//preceding-sibling::<tag>   przed rodzicem
# xpath-to-some-element//following-sibling::<tag>   za rodzicem
# używamy gdy nie ma możliwości namierzenia bezpośrednio
# //a[@href='/sign-in']
# //a[@href='/sign-in']//parent::li
# //a[@href='/sign-in']//parent::li//preceding-sibling::li//following-sibling::li[2]


# przykład ze strony
# //a[@href='/login']
# //a[@href='/login']//parent::div
# //a[@href='/login']//parent::div//preceding-sibling::div//following-sibling::div

# //input[@id='bmwradio']
# //input[@id='bmwradio']//parent::div//preceding-sibling::div

# //table[@id='product']//td[text()='Python Programming Language']//following-sibling::td - szukamy ceny programowania z tabeli







