import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { ShowDataComponentComponent } from './show-data-component/show-data-component.component';
import { IndexComponent } from './index/index.component';

const routes: Routes = [
  {
      path:"",
      component: ShowDataComponentComponent,
  },
  {
      path:"**",
      component: PageNotFoundComponent,
  },
  {
      path:"",
      component: IndexComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
