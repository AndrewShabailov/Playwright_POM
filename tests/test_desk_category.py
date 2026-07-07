def test_customizable_desk_on_page(desk_page):
    desk_page.open_page()
    desk_page.check_presence_of_customizable_desk_on_page('Customizable Desk')


def test_corner_desk_left_sit_on_page(desk_page):
    desk_page.open_page()
    desk_page.check_presence_of_corner_desk_left_sit_on_page('Corner Desk Left Sit')


def test_acoustic_bloc_screens_on_page(desk_page):
    desk_page.open_page()
    desk_page.check_presence_of_acoustic_bloc_screens_on_page('Acoustic Bloc Screens')
