from views.Router import Router
from views.index_view import IndexView
from views.settings_view import SettingsView
from views.register import Register

from views.screen_lock import Screen_lock
router = Router()

router.routes = {
  "/screen_lock": Screen_lock,
  # "/home": Screen_lock,
  "/": IndexView,
  "/settings": SettingsView,
  "/register": Register,

}
