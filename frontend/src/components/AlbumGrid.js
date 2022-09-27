import React, { Component } from "react";
import { Table } from "reactstrap";




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

export default AlbumGrid;