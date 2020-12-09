"""Main plugin file - Handles the various routes"""

__author__ = "yeyus"

import logging

import routing
import xbmc
import xbmcaddon
import xbmcplugin
from xbmcgui import ListItem

from resources.lib import kodilogging
from resources.lib import kodiutils as ku
from resources.lib import canalsur

kodilogging.config()
logger = logging.getLogger(__name__)
plugin = routing.Plugin()
ADDON_NAME = xbmcaddon.Addon().getAddonInfo("name")

CATEGORY_PROGRAMAS = "Programas"

def get_arg(key, default=None):
    # type: (str, Any) -> Any
    """Get the argument value or default"""
    if default is None:
        default = ""
    return plugin.args.get(key, [default])[0]

def add_menu_item(method, label, args=None, art=None, info=None, directory=True):
    # type: (Callable, Union[str, int], dict, dict, dict, bool) -> None
    """wrapper for xbmcplugin.addDirectoryItem"""
    info = {} if info is None else info
    art = {} if art is None else art
    args = {} if args is None else args
    label = ku.localize(label) if isinstance(label, int) else label
    list_item = ListItem(label)
    list_item.setArt(art)
    if method == search and "q" in args:
        # saved search menu items can be removed via context menu
        list_item.addContextMenuItems([(
            ku.localize(32019),
            "XBMC.RunPlugin({})".format(plugin.url_for(search, delete=True, q=label))
        )])
    if method == play_film:
        list_item.setInfo("video", info)
        list_item.setProperty("IsPlayable", "true")
    xbmcplugin.addDirectoryItem(
        plugin.handle,
        plugin.url_for(method, **args),
        list_item,
        directory)

@plugin.route("/")
def index():
    # type: () -> None
    """Main menu"""
    #add_menu_item(ultimos, "Ultimos", art=ku.icon("programas.png"))  # Ultimos
    add_menu_item(programas, CATEGORY_PROGRAMAS, art=ku.icon("programas.png"))  # Programas    
    xbmcplugin.setPluginCategory(plugin.handle, ADDON_NAME)
    xbmcplugin.endOfDirectory(plugin.handle)

@plugin.route("/programas")
def programas():
    # type: () -> None
    """Lista de Programas por CanalSur."""
    href = get_arg("href", False)
    category = get_arg("category", CATEGORY_PROGRAMAS)  # Programas
    if not href:
        # Listado de Programas menu
        programas = canalsur.get_programas()
        for programa in programas:
            add_menu_item(programmes,
                            programa.nombre,
                            info={"plot": programa.descripcion},
                            args={"href": programa.id, "category": programa.nombre},
                            art=ku.art(bps.get_uri(programa.thumbnail())))
    else:
        # Lista de Capitulos del programa (href es programaId)
        capitulos = canalsur.get_capitulos(id=href)        
        for capitulo in capitulos:            
            add_menu_item(play_film,
                          capitulo.capitulo,
                          args={ 
                              "href": capitulo.id, 
                              "videoUrl": capitulo.url[0],
                              "capitulo": capitulo.capitulo,
                              "fecha": capitulo.fecha
                          },
                          info={
                              "plot": capitulo.capitulo
                          },
                          art=ku.art(capitulo.tapa),
                          directory=False)
        xbmcplugin.setContent(plugin.handle, "capitulos")
        xbmcplugin.addSortMethod(plugin.handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
        xbmcplugin.addSortMethod(plugin.handle, xbmcplugin.SORT_METHOD_VIDEO_YEAR)
    xbmcplugin.setPluginCategory(plugin.handle, category)
    xbmcplugin.endOfDirectory(plugin.handle)

@plugin.route("/play")
def play_film():
    # type: () -> None
    """Show playable item"""
    href = get_arg("href")
    video_url = get_arg("videoUrl")
    capitulo = get_arg("capitulo")
    fecha = get_arg("fecha")
    #bps.recents.append(href) - guardar reciente
    list_item = ListItem(path=video_url)
    list_item.setInfo("video", {
        "title": capitulo,
        "premiered": fecha
    })
    xbmcplugin.setResolvedUrl(plugin.handle, True, list_item)

def run():
    # type: () -> None
    """Main entry point"""
    plugin.run()