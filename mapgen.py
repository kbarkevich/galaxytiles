import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

import re

from tiles import TileList


PX_PER_TILE = 50
GRID_WIDTH = 18
GRID_HEIGHT = 18


def main():
    top = Tk()
    right = Frame(top)
    right.pack(side="right")

    newwindow = tk.Toplevel(top)
    tilepicker = TilePicker(newwindow)

    tiles = [[set_up_button(top, right, i, j, tilepicker) for j in range(GRID_WIDTH)] for i in range(GRID_HEIGHT)]

    floors = read_map()
    floor = floors[2]

    for row, row_contents in enumerate(floor):
        for column, tile in enumerate(row_contents):
            tiles[row][column].change_tile(tile[0], tile[1], tile[2], tile[3])

    save_map(floors)

    mainloop()


class TilePicker():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(side="right")
        self.COLS = 4
        self.i = 1
        self.load_tiles()

    def get_tile(self):
        return self.tile

    def select_tile(self, i):
        self.i = i
        self.load_tiles()

    def load_tiles(self):
        self.buttons = []
        self.images = []
        self.tiles = [x for x in dir(TileList) if x[0] != '_']
        
        for i, tiletype in enumerate(self.tiles):
            col = i % self.COLS
            row = int(i / self.COLS)
            tile = getattr(TileList, tiletype)
            image = ImageTk.PhotoImage(master=self.master, file='images/unknown.png')
            btn = Button(self.frame, image=image, text=f"({row}, {col})", compound=CENTER)
            btn.config(width=PX_PER_TILE, height=PX_PER_TILE, relief='solid', borderwidth=0)
            btn.grid(row=row, column=col, sticky="NWSE")
            self.buttons.append(btn)
            if 'IMG' in tile:
                img = Image.open(tile['IMG'])
                if i == self.i:
                    self.tile = tile
                    source = img.split()
                    if img.mode == 'RGB':
                        R, G, B = 0, 1, 2
                        constant = 1.5 # constant by which each pixel is divided
                        img = Image.merge(img.mode, (source[R].point(lambda q: q*constant),
                                                    source[G].point(lambda q: q/constant),
                                                    source[B].point(lambda q: q/constant)))
                    else:
                        R, G, B, A = 0, 1, 2, 3
                        constant = 1.5 # constant by which each pixel is divided
                        img = Image.merge(img.mode, (source[R].point(lambda q: q*constant),
                                                    source[G].point(lambda q: q/constant),
                                                    source[B].point(lambda q: q/constant),
                                                    source[A].point(lambda q: q)))
                image.paste(img)
                btn.configure(text='')
            else:
                img = Image.open('images/unknown.png')
                if i == self.i:
                    self.tile = tile
                    source = img.split()
                    if img.mode == 'RGB':
                        R, G, B = 0, 1, 2
                        constant = 1.5 # constant by which each pixel is divided
                        img = Image.merge(img.mode, (source[R].point(lambda q: q*constant),
                                                    source[G].point(lambda q: q/constant),
                                                    source[B].point(lambda q: q/constant)))
                    else:
                        R, G, B, A = 0, 1, 2, 3
                        constant = 1.5 # constant by which each pixel is divided
                        img = Image.merge(img.mode, (source[R].point(lambda q: q*constant),
                                                    source[G].point(lambda q: q/constant),
                                                    source[B].point(lambda q: q/constant),
                                                    source[A].point(lambda q: q)))
                image.paste(img)
                btn.configure(text=tile['NAME'])
            btn.bind('<ButtonRelease-1>', lambda _, _i=i: self.select_tile(_i))
            self.images.append(image)

    def close_windows(self):
        self.master.destroy()


def save_map(floors):
    with open('map2.txt', 'w') as file:
        def writeline(line):
            file.write(line+'\n')
        writeline('MAP = {}')
        writeline('')
        for i, floor in enumerate(floors):
            writeline(f'Floor{i+1} = {"{"}')
            for j, row in enumerate(floor):
                line = '\t{'
                for name, rot1, rot2, rot3, extras in row:
                    if name == '':
                        line += "{},"
                    elif extras == '':
                        line += "{" + f"Tiles.{name}, {rot1}, {rot2}, {rot3}" + "},"
                    else:
                        line += "{" + f"Tiles.{name}, {rot1}, {rot2}, {rot3}, {extras}" + "},"
                line = line[:-1] + ("}," if j <= len(row)-1 else "}")
                writeline(line)
            writeline("}")
            writeline("")
        for i in range(len(floors)):
            writeline(f"MAP[{i+1}] = Floor{i+1}")

def read_map():
    file = open('map.txt', 'r')
    lines = file.readlines()

    floors = []
    floor_open = False
    current_floor = []

    i=0
    for line in lines:
        i+=1
        if i > 1:
            if (not floor_open) and (line.find('{')>-1):
                floor_open = True
                current_floor = []
            elif floor_open and line[0] != '}':
                row_tiles = parse_tile_info(line)
                current_floor.append(row_tiles)
            elif floor_open:
                floor_open = False
                floors.append(current_floor)
    file.close()
    return floors


def parse_tile_info(line):
    start_floor_idx = line.find('{')
    curr_endpoint = start_floor_idx + 1
    tiles = []
    for item_start in [m.start() for m in re.finditer('{', line)]:
        if item_start < curr_endpoint:
            continue
        name = ""
        rot1 = ""
        rot2 = ""
        rot3 = ""
        extras = ""
        nested_extras = 0
        stage = 0
        for char in line[item_start+1:]:
            curr_endpoint += 1
            if char == "," and stage != 4:
                stage += 1
            elif stage == 0:
                if char == '}':
                    break
                name += char
            elif stage == 1:
                rot1 += char
            elif stage == 2:
                rot2 += char
            elif stage == 3:
                if char == '}':
                    break
                rot3 += char
            elif stage == 4:
                if char == '{':
                    nested_extras += 1
                    extras += char
                elif char == '}':
                    nested_extras -= 1
                    if nested_extras < 0:
                        break
                    extras += char
                else:
                    extras += char
        curr_endpoint += 1
        if name.find('.') != -1:
            name = name[name.find('.')+1:]
        tiles.append((name.strip(), rot1.strip(), rot2.strip(), rot3.strip(), extras.strip()))
    return tiles


class TileListbox(tk.Listbox):
    def __init__(self, parent, tile, *args, **kwargs):
        tk.Listbox.__init__(self, parent, *args, **kwargs)
        self.tile = tile
        self.popup_menu = tk.Menu(self, tearoff=0)
        self.popup_menu.add_command(label="Delete",
                                    command=tile.delete_tile)
        self.popup_menu.add_command(label="Rotate",
                                    command=tile.rotate_tile)

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()


class Tile:
    def __init__(self, button, master, tilepicker, image, x, y, tiletype=None, rot1=0, rot2=0, rot3=0):
        self.x = x
        self.y = y
        self.button = button
        self.image=image
        self.rot1 = rot1
        self.rot2 = rot2
        self.rot3 = rot3
        self.tiletype=tiletype
        self.listbox = TileListbox(master, self)
        self.tilepicker = tilepicker
        self.change_tile(tiletype, self.rot1, self.rot2, self.rot3)

    def _clicked(self, event):
        self.change_tile(self.tilepicker.get_tile())

    def _menu(self, event):
        print(f"Opening the menu from tile {self}")
        self.listbox.popup(event)

    def _rotate_tile(self, event):
        self.rotate_tile()

    def rotate_tile(self):
        if self.tiletype != '':
            self.rot2 += 90
            self.rot2 = self.rot2 if self.rot2 < 360 else 0
            self.reload_image()

    def delete_tile(self):
        self.change_tile('')

    def change_tile(self, tiletype=None, rot1='0', rot2='0', rot3='0'):
        self.tiletype=tiletype
        if tiletype != '':
            self.rot1 = int(rot1)
            self.rot2 = int(rot2)
            self.rot3 = int(rot3)
        else:
            self.rot1 = 0
            self.rot2 = 0
            self.rot3 = 0
        if tiletype is None or tiletype == '':
            self.type = TileList.Blank
        elif type(tiletype) == str:
            self.type = getattr(TileList, tiletype)
        else:
            self.type = tiletype
        self.reload_image()
        

    def reload_image(self):
        if 'IMG' in self.type:
            img = Image.open(self.type['IMG']).rotate(self.rot2)
            self.image.paste(img)
            self.button.configure(text='')
        else:
            img = Image.open('images/unknown.png')
            self.image.paste(img)
            self.button.configure(text=self.type['NAME'])

    def __str__(self):
        return f"{self.x}, {self.y}: {self.tiletype}"


def set_up_button(master, frame, x, y, tilepicker):
    blank_image = ImageTk.PhotoImage(master=master, file='images/unknown.png')
    btn = Button(frame, image=blank_image, text=f"({x}, {y})", compound=CENTER)
    btn.config(width=PX_PER_TILE, height=PX_PER_TILE, relief='solid', borderwidth=0)
    btn.grid(row=x, column=y, sticky="NWSE")
    tile = Tile(btn, master, tilepicker, blank_image, x, y)
    btn.bind('<ButtonRelease-1>', tile._clicked)
    btn.bind('<ButtonRelease-2>', tile._rotate_tile)
    btn.bind('<ButtonRelease-3>', tile._menu)
    return tile


if __name__ == '__main__':
    main()
