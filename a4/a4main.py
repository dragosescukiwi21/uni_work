from a4classes import myVectorRepository
from a4controller import Controller
from a4UI import UI
import a4tests

repoList = []

a4tests.runTests()

repo = myVectorRepository(repoList)
controller = Controller(repo)
ui = UI(controller, repo)

ui.menu()
