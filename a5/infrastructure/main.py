import testing.tests as tests
from domain.plane import PlaneRepository
from domain.passengers import PassengerRepository

from service.service import Service
from ui import UI

# Running tests
tests.runTests()


# Create repos and their lists
repoList = []
P_repoList = []

repo = PlaneRepository(repoList)
psg_repo = PassengerRepository(P_repoList)


# Initialize ui with controller and repos
controller = Service(repoList, P_repoList)
ui = UI(controller, repo, psg_repo)


# Run
ui.run()
