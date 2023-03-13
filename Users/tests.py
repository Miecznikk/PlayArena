from django.test import TestCase
from django.contrib.auth.models import User
from .models import Position, App_User, Player, Referee
from Teams.models import Team
from django.urls import reverse
from .forms import UserLoginForm, RegisterForm, ProfileEditForm
from Matches.models import Goal, Match

# Create your tests here.
#models
class PositionModelTests(TestCase):

    def setUp(self):
        self.position = Position.objects.create(title='Goalkeeper')

    def testPositionCorrectness(self):
        self.assertEqual(str(self.position), 'Goalkeeper')

class AppUserModelTest(TestCase):
    def setUp(self):
        self.app_user = App_User.objects.create(first_name='Jan', second_name='Paweł', last_name='Żuk')

    def testAppUserCorrectness(self):
        self.assertEqual(str(self.app_user), 'Jan Paweł Żuk')

class PlayerModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testuser1password')
        self.position = Position.objects.create(title='Center back defender')
        self.team = Team.objects.create(name='Team 1')
        self.player = Player.objects.create(first_name='Karol', second_name='Filip', last_name='Łukasiuk', user=self.user,
                                            position=self.position, shirt_number=37, team=self.team)

    def testPlayerCorrectness(self):
        self.assertEqual(str(self.player), 'Karol Filip Łukasiuk')

    def testGetAbsoluteUrl(self):
        url = reverse('users:player_detail', args=[self.player.id])
        self.assertEqual(self.player.get_absolute_url(), url)
"""
    def testGetScoredGoals(self):
        goal = Goal.objects.create(scorer=self.player)
        self.assertEqual(self.player.get_scored_goals(), 1)

    def testGetMotm(self):
        match = Match.objects.create(motm=self.player)
        self.assertEqual(self.player.get_motm(), 1)

"""

class RefereeModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testReferee', password='sedzia12345')

#views
class ViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.player = Player.objects.create(user=self.user, first_name='Test', last_name='Player')
        self.team = Team.objects.create(name='Test Team')

    def testSignUpView(self):
        pass
        '''
        response = self.client.post(reverse('registration/sign_up.html'), {
            'username':'newUser',
            'password1':'newpassword',
            'password2':'newpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/home')
        self.assertEqual(User.objects.count(), 2)
        self.assertTrue(User.objects.filter(username='newUser').exists())
        '''

    def testHomeView(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def testPlayerDetailView(self):
        pass
        '''
        response = self.client.get(reverse('player-detail', args=[self.player.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'players/player_detail.html')
        self.assertEqual(response.context['player'], self.player)
        '''
#forms
class UserLoginFormTest(TestCase):

    def testUserLoginFormIsValid(self):
        form = UserLoginForm(data={'username': 'testuser', 'password': 'testpassword'})
        self.assertTrue(form.is_valid())

    def testUserLoginFormIsInvalid(self):
        form = UserLoginForm(data={'username': '', 'password': 'testpassword'})
        self.assertFalse(form.is_valid())

class RegisterFormTest(TestCase):

    def testRegisterFormIsValid(self):
        form = RegisterForm(data={'username': 'testuser', 'firstname': 'Test', 'last_name': 'User',
                                  'password1': 'testpassword', 'password2': 'testpassword', 'position': '1'})
        self.assertTrue(form.is_valid())

    def testRegisterFormIsInvalid(self):
        form = RegisterForm(data={'username': '', 'firstname': 'Test', 'last_name': 'User',
                                  'password1': 'testpassword', 'password2': 'testpassword', 'position': '1'})
        self.assertFalse(form.is_valid())

class ProfileEditFormTest(TestCase):

    def setUp(self):
        pass

    def testProfileEditFormIsValid(self):
        pass

    def testProfileEditFormIsInvalid(self):
        pass