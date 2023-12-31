import { fireEvent, render, screen, act } from "@testing-library/react";
import "@testing-library/jest-dom";
import { Provider } from "react-redux";
import { store } from "@redux/store";
import Login from "@pages/login";

describe("<Login/>", () => {
  beforeEach(() => {
    render(
      <Provider store={store}>
        <Login />
      </Provider>
    );
  });

  it("renders title correctly", () => {
    expect(screen.getByRole("heading")).toBeInTheDocument();
  });

  it("renders inputs correctly", () => {
    expect(screen.getByLabelText("Email")).toBeInTheDocument();
    expect(screen.getByLabelText("Password")).toBeInTheDocument();

    expect(screen.getByPlaceholderText("jiva@gmail.com")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("password")).toBeInTheDocument();
  });

  it("renders button correctly", () => {
    const button = screen.getByRole("button");
    expect(button).toBeInTheDocument();
    expect(button.getAttribute("type")).toBe("submit");
  });

  it("renders form validation", async () => {
    const button = screen.getByRole("button", { name: "Masuk" });
    await act(async () => {
      await fireEvent.click(button);
    });
    expect(screen.getByText("Email wajib diisi")).toBeInTheDocument();
    expect(screen.getByText("Password wajib diisi")).toBeInTheDocument();

    const emailInput = screen.getByLabelText("Email");
    await act(async () => {
      await fireEvent.change(emailInput, { target: { value: "dummy" } });
    });
    await act(async () => {
      await fireEvent.click(button);
    });
    expect(screen.getByText("Masukkan email yang valid")).toBeInTheDocument();
  });

  it("submits correctly", async () => {
    const emailInput = screen.getByLabelText("Email");
    const passwordInput = screen.getByLabelText("Password");

    const DUMMY_TEXT = "dummy@email.com";
    const options = {
      target: { value: DUMMY_TEXT },
    };

    await act(async () => {
      await fireEvent.change(emailInput, options);
      await fireEvent.change(passwordInput, options);
    });

    const button = screen.getByRole("button", { name: "Masuk" });
    await act(async () => {
      await fireEvent.click(button);
    });

    expect(store.getState().auth.accessToken).toBeUndefined();
  });
});
