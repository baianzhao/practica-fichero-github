
import tkinter as tk
import math

class GeometryDashCubeShipOnly:
    def __init__(self, root):
        self.root = root
        self.root.title("GD: Cube & Ship Mastery")
        self.ancho, self.alto = 1000, 450
        self.suelo_y = 380
        self.gravedad_normal = True # True: abajo (Azul), False: arriba (Amarillo)
        
        self.canvas = tk.Canvas(root, width=self.ancho, height=self.alto, bg="#001A2E", highlightthickness=0)
        self.canvas.pack()

        # Jugador
        self.modo = "CUBE" 
        self.jugando = True
        self.px, self.py = 150, 300
        self.vel_y = 0
        self.angulo = 0
        self.espacio = False
        self.distancia = 0
        self.meta_dist = 22000 # Nivel largo
        
        # --- LAYOUT SIN BOLA (Solo Cubo y Nave) ---
        self.layout = [
            (600, "pincho"), (1100, "pincho"), (1600, "bloque"), (1650, "bloque"),
            (2100, "triple_pincho"), (2800, "PORTAL_YELLOW"), # Cubo al techo
            (3500, "pincho_techo"), (4200, "bloque_techo"), (4800, "PORTAL_BLUE"), # Cubo al suelo
            (5500, "PORTAL_SHIP"), # Inicio Nave
            (6500, "pilar_vuelo"), (7500, "PORTAL_YELLOW"), # Nave al techo
            (8500, "pilar_vuelo_techo"), (9500, "pilar_vuelo_techo"), 
            (10500, "PORTAL_BLUE"), # Nave al suelo
            (12000, "PORTAL_CUBE"), # Vuelve Cubo
            (13000, "triple_pincho"), (14000, "bloque_alto"), (15000, "PORTAL_YELLOW"),
            (16500, "bloque_techo"), (17500, "PORTAL_BLUE"),
            (19000, "PORTAL_SHIP"), # Vuelo final
            (20000, "pilar_vuelo_doble"), (21500, "meta")
        ]
        
        self.entidades = []
        self.player = self.canvas.create_polygon([0,0,0,0], fill="#FFFB00", outline="white", width=2)
        self.ui_progreso = self.canvas.create_text(500, 30, text="0%", font=("Impact", 20), fill="white")
        self.canvas.create_rectangle(0, self.suelo_y, self.ancho, self.alto, fill="#0A0A0A")

        self.root.bind("<KeyPress-space>", lambda e: self.set_espacio(True))
        self.root.bind("<KeyRelease-space>", lambda e: self.set_espacio(False))
        
        self.run()

    def set_espacio(self, val): self.espacio = val

    def get_player_pts(self):
        rad = math.radians(self.angulo)
        if self.modo == "CUBE":
            pts = [(-15,-15),(15,-15),(15,15),(-15,15)]
        else: # SHIP
            pts = [(25,0), (-15,-12), (-5,0), (-15,12)]
        
        res = []
        for dx, dy in pts:
            nx = dx * math.cos(rad) - dy * math.sin(rad)
            ny = dx * math.sin(rad) + dy * math.cos(rad)
            if not self.gravedad_normal: ny = -ny # Inversión visual
            res.extend([self.px + nx, self.py + ny])
        return res

    def spawn_engine(self):
        while self.layout and self.distancia >= self.layout[0][0]:
            dist, tipo = self.layout.pop(0)
            x = self.ancho
            if tipo == "pincho":
                self.entidades.append((self.canvas.create_polygon(x, self.suelo_y, x+30, self.suelo_y, x+15, self.suelo_y-30, fill="#FF4444"), "pincho"))
            elif tipo == "pincho_techo":
                self.entidades.append((self.canvas.create_polygon(x, 0, x+30, 0, x+15, 30, fill="#FF4444"), "pincho"))
            elif tipo == "bloque":
                self.entidades.append((self.canvas.create_rectangle(x, self.suelo_y-40, x+45, self.suelo_y, fill="#555", outline="white"), "bloque"))
            elif tipo == "bloque_alto":
                self.entidades.append((self.canvas.create_rectangle(x, self.suelo_y-80, x+50, self.suelo_y, fill="#555", outline="white"), "bloque"))
            elif tipo == "bloque_techo":
                self.entidades.append((self.canvas.create_rectangle(x, 0, x+45, 40, fill="#555", outline="white"), "bloque"))
            elif tipo == "triple_pincho":
                for i in range(3):
                    self.entidades.append((self.canvas.create_polygon(x+(i*32), self.suelo_y, x+30+(i*32), self.suelo_y, x+15+(i*32), self.suelo_y-30, fill="#FF4444"), "pincho"))
            elif tipo == "PORTAL_YELLOW":
                self.entidades.append((self.canvas.create_rectangle(x, 50, x+40, 350, fill="#FFFF00", outline="white", stipple="gray50"), "p_yellow"))
            elif tipo == "PORTAL_BLUE":
                self.entidades.append((self.canvas.create_rectangle(x, 50, x+40, 350, fill="#0000FF", outline="white", stipple="gray50"), "p_blue"))
            elif tipo == "PORTAL_SHIP":
                self.entidades.append((self.canvas.create_rectangle(x, 50, x+50, 350, fill="#A020F0", outline="white"), "portal_ship"))
            elif tipo == "PORTAL_CUBE":
                self.entidades.append((self.canvas.create_rectangle(x, 50, x+50, 350, fill="#20A0F0", outline="white"), "portal_cube"))
            elif tipo == "pilar_vuelo":
                self.entidades.append((self.canvas.create_rectangle(x, 0, x+50, 140, fill="#444", outline="white"), "bloque"))
                self.entidades.append((self.canvas.create_rectangle(x, 300, x+50, self.suelo_y, fill="#444", outline="white"), "bloque"))
            elif tipo == "pilar_vuelo_techo":
                self.entidades.append((self.canvas.create_rectangle(x, 180, x+50, self.suelo_y, fill="#444", outline="white"), "bloque"))
            elif tipo == "pilar_vuelo_doble":
                self.entidades.append((self.canvas.create_rectangle(x, 0, x+50, 100, fill="#444"), "bloque"))
                self.entidades.append((self.canvas.create_rectangle(x, 350, x+50, self.suelo_y, fill="#444"), "bloque"))
            elif tipo == "meta":
                self.entidades.append((self.canvas.create_rectangle(x, 0, x+100, self.suelo_y, fill="#00FF7F"), "meta"))

    def run(self):
        if not self.jugando: return
        self.distancia += 12 # Velocidad ligeramente aumentada
        
        porcentaje = min(100, int((self.distancia / self.meta_dist) * 100))
        self.canvas.itemconfig(self.ui_progreso, text=f"{porcentaje}%")

        # --- FÍSICAS ---
        g_mult = 1 if self.gravedad_normal else -1
        
        if self.modo == "CUBE":
            self.vel_y += 1.8 * g_mult
        else: # SHIP
            impulso = -2.3 if self.espacio else 1.7
            self.vel_y += impulso * g_mult
            self.vel_y *= 0.94
            self.angulo = max(-35, min(35, self.vel_y * 4))
        
        self.py += self.vel_y
        
        en_contacto = False
        if self.py >= self.suelo_y - 15:
            self.py, self.vel_y, en_contacto = self.suelo_y - 15, 0, True
        elif self.py <= 30:
            self.py, self.vel_y, en_contacto = 30, 0, True

        if self.modo == "CUBE" and self.espacio and en_contacto:
            self.vel_y = -17.5 * g_mult

        # --- COLISIONES ---
        p_box = (self.px-12, self.py-12, self.px+12, self.py+12)
        
        for item in self.entidades[:]:
            obj_id, tipo = item
            self.canvas.move(obj_id, -12, 0)
            c = self.canvas.coords(obj_id)
            if not c or c[0] < -100:
                self.canvas.delete(obj_id)
                self.entidades.remove(item)
                continue
            
            o_box = (c[0], c[1], c[2], c[3]) if len(c)==4 else (c[0], c[5], c[2], c[1])
            
            if not (p_box[2] < o_box[0] or p_box[0] > o_box[2] or p_box[3] < o_box[1] or p_box[1] > o_box[3]):
                if tipo == "pincho": self.morir()
                elif tipo == "meta": self.victoria()
                elif tipo == "portal_ship": self.modo = "SHIP"
                elif tipo == "portal_cube": 
                    self.modo = "CUBE"
                    self.angulo = 0
                elif tipo == "p_yellow": self.gravedad_normal = False
                elif tipo == "p_blue":   self.gravedad_normal = True
                elif tipo == "bloque":
                    if self.gravedad_normal and p_box[3] <= o_box[1]+12 and self.vel_y >= 0:
                        self.py, self.vel_y = o_box[1]-15, 0
                    elif not self.gravedad_normal and p_box[1] >= o_box[3]-12 and self.vel_y <= 0:
                        self.py, self.vel_y = o_box[3]+15, 0
                    elif p_box[2] > o_box[0]+6: self.morir()

        if self.modo == "CUBE" and not en_contacto: self.angulo += 14 * g_mult
        elif en_contacto: self.angulo = 0

        self.canvas.coords(self.player, self.get_player_pts())
        self.spawn_engine()
        self.root.after(16, self.run)

    def morir(self):
        self.jugando = False
        self.canvas.create_text(500, 200, text="GAME OVER", font=("Impact", 70), fill="red")
        self.root.bind("r", lambda e: self.reiniciar())

    def victoria(self):
        self.jugando = False
        self.canvas.create_text(500, 200, text="LEVEL COMPLETE", font=("Impact", 60), fill="#00FF7F")
        self.root.bind("r", lambda e: self.reiniciar())

    def reiniciar(self):
        self.canvas.delete("all")
        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    GeometryDashCubeShipOnly(root)
    root.mainloop()
