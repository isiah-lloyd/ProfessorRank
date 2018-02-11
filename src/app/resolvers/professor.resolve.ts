import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot } from '@angular/router';
import { ProfessorService } from '../professor.service';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import 'rxjs/add/operator/delay';

@Injectable()
export class ProfessorResolver implements Resolve<any> {
  constructor(private professorService: ProfessorService) {}

  resolve(route: ActivatedRouteSnapshot) {
    return this.professorService.getProfessor(route.paramMap.get("id"));
  }
}