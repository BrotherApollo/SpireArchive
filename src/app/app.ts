import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [FormsModule, CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  players = ['Kenji', 'Caleb'];
  characters = ['Ironclad', 'Silent', 'Regent', 'Necrobinder', 'Defect'];
  difficulties = ['0', '1', '2'];

  player1 = '';
  character1 = '';
  player2 = '';
  character2 = '';
  floorsCleared = 0;
  difficulty = '';
  won = false;

  submitRun(): void {
    console.log({
      player1: this.player1,
      character1: this.character1,
      player2: this.player2,
      character2: this.character2,
      floorsCleared: this.floorsCleared,
      difficulty: this.difficulty,
      won: this.won
    });
  }
}