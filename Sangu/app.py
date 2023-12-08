import tkinter as tk
from tkinter import messagebox

class VotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.voters = set()
        self.votes = {candidate: 0 for candidate in candidates}

    def vote(self, candidate, voter):
        if voter in self.voters:
            messagebox.showinfo("Error", "You have already voted.")
        elif candidate not in self.candidates:
            messagebox.showinfo("Error", "Invalid candidate.")
        else:
            self.votes[candidate] += 1
            self.voters.add(voter)
            messagebox.showinfo("Success", "Vote cast successfully.")

    def get_results(self):
        results = "\n".join([f"{candidate}: {self.votes[candidate]} votes" for candidate in self.candidates])
        return results

class VotingApp:
    def __init__(self, master, voting_system):
        self.master = master
        self.voting_system = voting_system

        self.label = tk.Label(master, text="Select your candidate:")
        self.label.pack()

        self.candidate_var = tk.StringVar()
        self.candidate_var.set(voting_system.candidates[0])

        self.candidate_menu = tk.OptionMenu(master, self.candidate_var, *voting_system.candidates)
        self.candidate_menu.pack()

        self.vote_button = tk.Button(master, text="Vote", command=self.cast_vote)
        self.vote_button.pack()

        self.result_button = tk.Button(master, text="Get Results", command=self.show_results)
        self.result_button.pack()

    def cast_vote(self):
        candidate = self.candidate_var.get()
        voter = hash(candidate)  # Simulating a simple voter ID for demonstration purposes
        self.voting_system.vote(candidate, voter)

    def show_results(self):
        results = self.voting_system.get_results()
