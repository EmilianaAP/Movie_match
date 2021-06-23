import Registration
import Movie_matching
import Friend_list

def Test_function():
    assert 0 == Registration.login('Emito312', 'PenchoEGotin')
    assert 0 == Registration.register('Coraline', 'Password')
    assert 0 == Friend_list.add_friend('Emito312', 'Coraline')
    assert 0 == Movie_matching.match('Emito', 'Adito312')


if __name__ == '__main__':
    Test_function()
    print("Everything works properly.")