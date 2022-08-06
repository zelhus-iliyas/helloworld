import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  // template:'<h1>Iliyas</h1>',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'newapp';
  //interpolation
  pageTitle: string = 'Iliyas!';
  //propertybinding
  imageUrl = 'assets/images/iliyas.jpg';
  //eventbinding
  hello() {
    alert('Holaa,Mi amoru.');
  }
  username: string = '';
}
