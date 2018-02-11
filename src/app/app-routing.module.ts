import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProfessorComponent } from "./professor/professor.component";
import { ProfessorResolver } from "./resolvers/professor.resolve"

const routes: Routes = [
  {
    path: 'professor/:id',
    component: ProfessorComponent,
    resolve: {payload: ProfessorResolver}
  }
];
@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  providers: [ProfessorResolver]
})
export class AppRoutingModule {}
