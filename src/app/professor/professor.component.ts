import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";

@Component({
  templateUrl: './professor.component.html',
  styleUrls: ['./professor.component.css']
})
export class ProfessorComponent implements OnInit {
  payload: object;
  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    this.payload = this.route.snapshot.data.payload
  }
}
