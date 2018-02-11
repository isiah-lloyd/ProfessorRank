import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import { Observer } from 'rxjs/Observer';
const API_ENDPOINT = "https://btm95uoh6g.execute-api.us-east-2.amazonaws.com/dev"
const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class ProfessorService {

  constructor(private http:HttpClient) { }

  getProfessor(id: string) {
    return this.http.get(API_ENDPOINT + `/professor/${id}`);
  }
  createProfessor(body: object) {
    JSON.stringify(body);
    return this.http.post(API_ENDPOINT + '/professor/create', body, httpOptions);
  }
}
