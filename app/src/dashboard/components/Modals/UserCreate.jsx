const UserCreate = () => {
  return (
    <div
      className="modal fade show"
      id="exampleModalCenteredScrollable"
      tabIndex="-1"
      aria-labelledby="exampleModalCenteredScrollableTitle"
      style={{display: "none"}} //cambiar a display block para ver el modal
      aria-modal="true"
      role="dialog"
    >
      <div className="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title" id="exampleModalCenteredScrollableTitle">
              Modal title
            </h5>
            <button
              type="button"
              className="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div className="modal-body">
            <p>
              This is some placeholder content to show a vertically centered
              modal. We've added some extra copy here to show how vertically
              centering the modal works when combined with scrollable modals. We
              also use some repeated line breaks to quickly extend the height of
              the content, thereby triggering the scrolling. When content
              becomes longer than the prefedined max-height of modal, content
              will be cropped and scrollable within the modal.
            </p>
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <p>Just like that.</p>
          </div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <button type="button" className="btn btn-primary">
              Save changes
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserCreate;
