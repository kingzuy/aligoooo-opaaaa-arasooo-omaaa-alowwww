"""Water Bucket Puzzle - Desktop GUI Version
Original by Al Sweigart al@inventwithpython.com
Enhanced with Tkinter GUI and exception handling
"""

import random
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from typing import Dict, List


class WaterBucketGUI:
    """GUI version of Water Bucket Puzzle using Tkinter"""

    def __init__(self, root):
        """Initialize the GUI application

        Args:
            root: Tkinter root window
        """
        try:
            self.root = root
            self.root.title("💧 Water Bucket Puzzle")
            self.root.geometry("1100x800")
            self.root.resizable(False, False)

            # Game state
            self.bucket_sizes = {"8": 8, "5": 5, "3": 3}
            self.water_in_bucket = {"8": 0, "5": 0, "3": 0}
            self.goal = 4
            self.steps = 0
            self.history = []
            self.difficulty = "easy"

            # Colors - Improved contrast
            self.bg_color = "#F5F5F5"
            self.water_color = "#1976D2"
            self.empty_color = "#FFFFFF"
            self.border_color = "#0D47A1"

            # Setup UI
            self.setup_ui()
            self.update_display()

        except Exception as e:
            messagebox.showerror(
                "Initialization Error", f"Failed to initialize game: {e}"
            )

    def setup_ui(self):
        """Setup all UI components"""
        try:
            self.root.configure(bg=self.bg_color)

            # Title
            title_frame = tk.Frame(self.root, bg=self.bg_color)
            title_frame.pack(pady=15)

            tk.Label(
                title_frame,
                text="💧 Water Bucket Puzzle",
                font=("Arial", 28, "bold"),
                bg=self.bg_color,
                fg="#0D47A1",
            ).pack()

            tk.Label(
                title_frame,
                text="Dapatkan jumlah air yang tepat di salah satu ember!",
                font=("Arial", 12),
                bg=self.bg_color,
                fg="#212121",
            ).pack()

            # Difficulty selection
            self.setup_difficulty_frame()

            # Stats frame
            self.setup_stats_frame()

            # Buckets display
            self.setup_buckets_frame()

            # Control buttons
            self.setup_control_frame()

            # Action buttons
            self.setup_action_frame()

            # History panel
            self.setup_history_frame()

        except Exception as e:
            messagebox.showerror("UI Setup Error", f"Failed to setup UI: {e}")

    def setup_difficulty_frame(self):
        """Setup difficulty selection frame"""
        try:
            diff_frame = tk.LabelFrame(
                self.root,
                text="Tingkat Kesulitan",
                font=("Arial", 11, "bold"),
                bg=self.bg_color,
                fg="#0D47A1",
                padx=15,
                pady=10,
            )
            diff_frame.pack(pady=10, padx=30, fill="x")

            difficulties = [
                ("Easy - Target: 4L (8L, 5L, 3L)", "easy"),
                ("Medium - Target: 6L (10L, 7L, 3L)", "medium"),
                ("Hard - Target: 5L (12L, 8L, 5L)", "hard"),
            ]

            for text, value in difficulties:
                btn = tk.Button(
                    diff_frame,
                    text=text,
                    command=lambda v=value: self.change_difficulty(v),
                    bg="#1976D2" if value == "easy" else "#42A5F5",
                    fg="#FFFFFF",
                    activebackground="#0D47A1",
                    activeforeground="#FFFFFF",
                    font=("Arial", 10, "bold"),
                    relief="raised",
                    bd=3,
                    padx=15,
                    pady=10,
                    cursor="hand2",
                )
                btn.pack(side="left", padx=8, expand=True, fill="x")

        except Exception as e:
            print(f"Error setting up difficulty frame: {e}")

    def setup_stats_frame(self):
        """Setup statistics display frame"""
        try:
            stats_frame = tk.Frame(self.root, bg=self.bg_color)
            stats_frame.pack(pady=10, padx=30, fill="x")

            # Steps counter
            steps_frame = tk.Frame(
                stats_frame, bg="#FFFFFF", relief="solid", bd=3, highlightthickness=0
            )
            steps_frame.pack(side="left", padx=10, fill="both", expand=True)

            tk.Label(
                steps_frame,
                text="Langkah",
                font=("Arial", 12, "bold"),
                bg="#FFFFFF",
                fg="#424242",
            ).pack(pady=5)

            self.steps_label = tk.Label(
                steps_frame,
                text="0",
                font=("Arial", 32, "bold"),
                bg="#FFFFFF",
                fg="#1976D2",
            )
            self.steps_label.pack(pady=10)

            # Goal display
            goal_frame = tk.Frame(
                stats_frame, bg="#FFFFFF", relief="solid", bd=3, highlightthickness=0
            )
            goal_frame.pack(side="left", padx=10, fill="both", expand=True)

            tk.Label(
                goal_frame,
                text="Target",
                font=("Arial", 12, "bold"),
                bg="#FFFFFF",
                fg="#424242",
            ).pack(pady=5)

            self.goal_label = tk.Label(
                goal_frame,
                text="4L",
                font=("Arial", 32, "bold"),
                bg="#FFFFFF",
                fg="#2E7D32",
            )
            self.goal_label.pack(pady=10)

        except Exception as e:
            print(f"Error setting up stats frame: {e}")

    def setup_buckets_frame(self):
        """Setup buckets visualization frame"""
        try:
            buckets_frame = tk.LabelFrame(
                self.root,
                text="Ember Air",
                font=("Arial", 11, "bold"),
                bg=self.bg_color,
                fg="#0D47A1",
                padx=15,
                pady=15,
            )
            buckets_frame.pack(pady=10, padx=30, fill="both", expand=True)

            # Canvas for buckets
            self.canvas = tk.Canvas(
                buckets_frame,
                width=1000,
                height=280,
                bg="#FAFAFA",
                highlightthickness=2,
                highlightbackground="#BDBDBD",
            )
            self.canvas.pack()

        except Exception as e:
            print(f"Error setting up buckets frame: {e}")

    def setup_control_frame(self):
        """Setup bucket control buttons frame"""
        try:
            control_frame = tk.Frame(self.root, bg=self.bg_color)
            control_frame.pack(pady=10, padx=30, fill="x")

            self.bucket_buttons = {}

            for i, (key, size) in enumerate(
                sorted(self.bucket_sizes.items(), key=lambda x: int(x[0]), reverse=True)
            ):
                bucket_frame = tk.Frame(control_frame, bg=self.bg_color)
                bucket_frame.pack(side="left", padx=20, expand=True)

                tk.Label(
                    bucket_frame,
                    text=f"Ember {size}L",
                    font=("Arial", 11, "bold"),
                    bg=self.bg_color,
                    fg="#212121",
                ).pack(pady=5)

                btn_frame = tk.Frame(bucket_frame, bg=self.bg_color)
                btn_frame.pack(pady=5)

                fill_btn = tk.Button(
                    btn_frame,
                    text="ISI",
                    command=lambda k=key: self.fill_bucket(k),
                    bg="#1976D2",
                    fg="#000000",
                    activebackground="#0D47A1",
                    activeforeground="#000000",
                    font=("Arial", 10, "bold"),
                    width=10,
                    relief="raised",
                    bd=3,
                    cursor="hand2",
                )
                fill_btn.pack(side="left", padx=3)

                empty_btn = tk.Button(
                    btn_frame,
                    text="KOSONG",
                    command=lambda k=key: self.empty_bucket(k),
                    bg="#D32F2F",
                    fg="#000000",
                    activebackground="#B71C1C",
                    activeforeground="#000000",
                    font=("Arial", 10, "bold"),
                    width=10,
                    relief="raised",
                    bd=3,
                    cursor="hand2",
                )
                empty_btn.pack(side="left", padx=3)

        except Exception as e:
            print(f"Error setting up control frame: {e}")

    def setup_action_frame(self):
        """Setup action buttons frame"""
        try:
            action_frame = tk.Frame(self.root, bg=self.bg_color)
            action_frame.pack(pady=10, padx=30, fill="x")

            # Pour buttons
            pour_label = tk.Label(
                action_frame,
                text="Tuang Air:",
                font=("Arial", 11, "bold"),
                bg=self.bg_color,
                fg="#212121",
            )
            pour_label.pack(side="left", padx=10)

            bucket_list = sorted(
                self.bucket_sizes.keys(), key=lambda x: int(x), reverse=True
            )

            for src in bucket_list:
                for dst in bucket_list:
                    if src != dst:
                        btn = tk.Button(
                            action_frame,
                            text=f"{src}L → {dst}L",
                            command=lambda s=src, d=dst: self.pour_bucket(s, d),
                            bg="#7B1FA2",
                            fg="#FFFFFF",
                            activebackground="#4A148C",
                            activeforeground="#FFFFFF",
                            font=("Arial", 10, "bold"),
                            width=11,
                            relief="raised",
                            bd=3,
                            cursor="hand2",
                        )
                        btn.pack(side="left", padx=3)

            # Utility buttons
            hint_btn = tk.Button(
                action_frame,
                text="💡 HINT",
                command=self.show_hint,
                bg="#F57C00",
                fg="#FFFFFF",
                activebackground="#E65100",
                activeforeground="#FFFFFF",
                font=("Arial", 10, "bold"),
                width=12,
                relief="raised",
                bd=3,
                cursor="hand2",
            )
            hint_btn.pack(side="right", padx=5)

            reset_btn = tk.Button(
                action_frame,
                text="🔄 RESET",
                command=self.reset_game,
                bg="#424242",
                fg="#FFFFFF",
                activebackground="#212121",
                activeforeground="#FFFFFF",
                font=("Arial", 10, "bold"),
                width=12,
                relief="raised",
                bd=3,
                cursor="hand2",
            )
            reset_btn.pack(side="right", padx=5)

        except Exception as e:
            print(f"Error setting up action frame: {e}")

    def setup_history_frame(self):
        """Setup history display frame"""
        try:
            history_frame = tk.LabelFrame(
                self.root,
                text="📜 Riwayat Langkah",
                font=("Arial", 11, "bold"),
                bg=self.bg_color,
                fg="#0D47A1",
                padx=15,
                pady=10,
            )
            history_frame.pack(pady=10, padx=30, fill="both", expand=True)

            self.history_text = scrolledtext.ScrolledText(
                history_frame,
                height=10,
                width=100,
                font=("Consolas", 10),
                bg="#FFFFFF",
                fg="#212121",
                relief="solid",
                bd=2,
                wrap=tk.WORD,
            )
            self.history_text.pack(fill="both", expand=True)
            self.history_text.config(state="disabled")

        except Exception as e:
            print(f"Error setting up history frame: {e}")

    def draw_buckets(self):
        """Draw all buckets on canvas"""
        try:
            self.canvas.delete("all")

            bucket_list = sorted(
                self.bucket_sizes.items(), key=lambda x: int(x[0]), reverse=True
            )

            x_start = 150
            x_spacing = 300

            for i, (key, size) in enumerate(bucket_list):
                x = x_start + (i * x_spacing)
                self.draw_bucket(x, key, size, self.water_in_bucket[key])

        except Exception as e:
            print(f"Error drawing buckets: {e}")

    def draw_bucket(self, x, key, size, water):
        """Draw a single bucket with water

        Args:
            x: X position
            key: Bucket key
            size: Bucket size
            water: Amount of water in bucket
        """
        try:
            # Bucket dimensions
            width = 120
            height = 220
            y_bottom = 250
            y_top = y_bottom - height

            # Draw bucket outline
            self.canvas.create_rectangle(
                x - width // 2,
                y_top,
                x + width // 2,
                y_bottom,
                outline=self.border_color,
                width=5,
                fill=self.empty_color,
            )

            # Draw water
            if water > 0:
                water_height = (water / size) * height
                water_y = y_bottom - water_height

                self.canvas.create_rectangle(
                    x - width // 2 + 3,
                    water_y,
                    x + width // 2 - 3,
                    y_bottom - 3,
                    fill=self.water_color,
                    outline="",
                )

            # Draw capacity label
            self.canvas.create_text(
                x,
                y_bottom + 20,
                text=f"{size}L",
                font=("Arial", 16, "bold"),
                fill="#212121",
            )

            # Draw current amount
            self.canvas.create_text(
                x,
                y_top - 20,
                text=f"{water}L",
                font=("Arial", 14, "bold"),
                fill=self.water_color if water > 0 else "#9E9E9E",
            )

            # Draw water level marks
            for i in range(1, size + 1):
                mark_y = y_bottom - (i / size) * height
                self.canvas.create_line(
                    x - width // 2 - 8,
                    mark_y,
                    x - width // 2,
                    mark_y,
                    fill="#424242",
                    width=3,
                )
                self.canvas.create_text(
                    x - width // 2 - 20,
                    mark_y,
                    text=str(i),
                    font=("Arial", 9, "bold"),
                    fill="#424242",
                )

        except Exception as e:
            print(f"Error drawing bucket: {e}")

    def fill_bucket(self, bucket):
        """Fill a bucket to capacity"""
        try:
            size = self.bucket_sizes[bucket]
            old_amount = self.water_in_bucket[bucket]

            if old_amount == size:
                messagebox.showinfo("Info", f"Ember {size}L sudah penuh!")
                return

            self.water_in_bucket[bucket] = size
            self.steps += 1

            action = f"Mengisi ember {size}L penuh (dari {old_amount}L ke {size}L)"
            self.add_to_history(action)
            self.update_display()
            self.check_win()

        except KeyError:
            messagebox.showerror("Error", f"Ember tidak valid: {bucket}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengisi ember: {e}")

    def empty_bucket(self, bucket):
        """Empty a bucket completely"""
        try:
            size = self.bucket_sizes[bucket]
            old_amount = self.water_in_bucket[bucket]

            if old_amount == 0:
                messagebox.showinfo("Info", f"Ember {size}L sudah kosong!")
                return

            self.water_in_bucket[bucket] = 0
            self.steps += 1

            action = f"Mengosongkan ember {size}L (sebelumnya {old_amount}L)"
            self.add_to_history(action)
            self.update_display()

        except KeyError:
            messagebox.showerror("Error", f"Ember tidak valid: {bucket}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengosongkan ember: {e}")

    def pour_bucket(self, src, dst):
        """Pour water from source to destination bucket"""
        try:
            src_size = self.bucket_sizes[src]
            dst_size = self.bucket_sizes[dst]
            src_water = self.water_in_bucket[src]
            dst_water = self.water_in_bucket[dst]

            if src_water == 0:
                messagebox.showinfo("Info", f"Ember sumber {src_size}L kosong!")
                return

            if dst_water == dst_size:
                messagebox.showinfo("Info", f"Ember tujuan {dst_size}L sudah penuh!")
                return

            empty_space = dst_size - dst_water
            amount_to_pour = min(empty_space, src_water)

            self.water_in_bucket[src] -= amount_to_pour
            self.water_in_bucket[dst] += amount_to_pour
            self.steps += 1

            action = (
                f"Menuang {amount_to_pour}L dari ember {src_size}L ke ember {dst_size}L"
            )
            self.add_to_history(action)
            self.update_display()
            self.check_win()

        except KeyError as e:
            messagebox.showerror("Error", f"Ember tidak valid: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menuang air: {e}")

    def check_win(self):
        """Check if puzzle is solved"""
        try:
            for size, amount in self.water_in_bucket.items():
                if amount == self.goal:
                    messagebox.showinfo(
                        "🎉 Selamat!",
                        f"Anda berhasil menyelesaikan puzzle!\n\n"
                        f"Jumlah langkah: {self.steps}\n"
                        f"Target: {self.goal}L tercapai di ember {self.bucket_sizes[size]}L",
                    )
                    return True
            return False

        except Exception as e:
            print(f"Error checking win: {e}")
            return False

    def add_to_history(self, action):
        """Add action to history display"""
        try:
            self.history.append(action)
            self.history_text.config(state="normal")
            self.history_text.insert("end", f"{len(self.history)}. {action}\n")
            self.history_text.see("end")
            self.history_text.config(state="disabled")

        except Exception as e:
            print(f"Error adding to history: {e}")

    def update_display(self):
        """Update all display elements"""
        try:
            self.steps_label.config(text=str(self.steps))
            self.goal_label.config(text=f"{self.goal}L")
            self.draw_buckets()

        except Exception as e:
            print(f"Error updating display: {e}")

    def reset_game(self):
        """Reset the game to initial state"""
        try:
            if messagebox.askyesno("Reset", "Yakin ingin reset permainan?"):
                for key in self.water_in_bucket:
                    self.water_in_bucket[key] = 0

                self.steps = 0
                self.history.clear()

                self.history_text.config(state="normal")
                self.history_text.delete(1.0, "end")
                self.history_text.config(state="disabled")

                self.update_display()
                messagebox.showinfo("Reset", "Permainan telah direset!")

        except Exception as e:
            messagebox.showerror("Error", f"Gagal reset permainan: {e}")

    def change_difficulty(self, difficulty):
        """Change game difficulty"""
        try:
            difficulties = {
                "easy": ({"8": 8, "5": 5, "3": 3}, 4),
                "medium": ({"10": 10, "7": 7, "3": 3}, 6),
                "hard": ({"12": 12, "8": 8, "5": 5}, 5),
            }

            if difficulty not in difficulties:
                raise ValueError(f"Invalid difficulty: {difficulty}")

            self.bucket_sizes, self.goal = difficulties[difficulty]
            self.water_in_bucket = {k: 0 for k in self.bucket_sizes.keys()}
            self.difficulty = difficulty
            self.steps = 0
            self.history.clear()

            self.history_text.config(state="normal")
            self.history_text.delete(1.0, "end")
            self.history_text.config(state="disabled")

            # Recreate control and action frames
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Frame) and widget != self.root:
                    widget.destroy()

            self.setup_ui()
            self.update_display()

            messagebox.showinfo(
                "Tingkat Kesulitan",
                f"Tingkat kesulitan diubah ke: {difficulty.upper()}\n"
                f"Target: {self.goal}L",
            )

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengubah tingkat kesulitan: {e}")

    def show_hint(self):
        """Show a helpful hint"""
        try:
            hints = [
                "💡 Coba isi ember terbesar terlebih dahulu",
                "💡 Gunakan ember terkecil untuk mengukur",
                "💡 Tuangkan air dari ember besar ke kecil",
                "💡 Kosongkan ember kecil saat penuh",
                "💡 Kombinasikan operasi isi-tuang-kosong",
                "💡 Kerja mundur dari target yang ingin dicapai",
            ]

            hint = random.choice(hints)
            messagebox.showinfo("Petunjuk", hint)

        except Exception as e:
            messagebox.showerror("Error", f"Gagal menampilkan petunjuk: {e}")


def main():
    """Main function to run the application"""
    try:
        root = tk.Tk()
        app = WaterBucketGUI(root)
        root.mainloop()

    except Exception as e:
        print(f"Fatal error: {e}")
        messagebox.showerror("Fatal Error", f"Aplikasi gagal berjalan: {e}")


if __name__ == "__main__":
    main()
