import React from "react";
import '../css/AlbumGrid.css';
import { Container } from "../styles/AlbumGrid.styles"


function AlbumGrid(albums) {
  console.log('AlbumGrid');
  console.log(albums)
  console.log(albums['albums'])
  albums = albums['albums']
  return (
    <Container style={{ 'grid-template-columns': `repeat(12, auto)`, 'grid-template-rows': `repeat(12, auto)` }}>
      {!albums || albums.length <= 0 ? (
        <tr>
          <td colSpan="6" align="center">
            <b>Ops, no one here yet</b>
          </td>
        </tr>
      ) : (
        albums.slice(0, 144).map(album => (

          <div class="grid-item"><img src={album.cover_art_url} /></div>

        ))
      )}
    </Container>
  );

}


export default AlbumGrid;

/*
class AlbumGrid extends Component {
  render() {
    const albums = this.props.albums;
    return (
      <Table dark>
        <tbody>
          {!albums || albums.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            albums.map(album => (
              <tr key={album.pk}>
                <td>{album.name}</td>
                <td>{album.email}</td>
                <td>{album.document}</td>
                <td>{album.phone}</td>
                <td>{album.registrationDate}</td>
                
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}
*/